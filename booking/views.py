from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import WorkSpace, Booking
from .forms import BookingForm, CheckBookingsForm


def home(request):
    """
    """
    booking_form = BookingForm()

    return render(
        request=request,
        template_name='booking/home.html',
        context={
            "booking_form": booking_form,
        },
    )

def book_workspace(request):
    """
    """
    if request.method == "POST":
        check_bookings_form = CheckBookingsForm(request.POST)

        if check_bookings_form.is_valid():
            date = check_bookings_form.cleaned_data['date']
            start_time = check_bookings_form.cleaned_data['start_time']
            end_time = check_bookings_form.cleaned_data['end_time']

            url = (
                reverse('home')
                + f"?date={date}&start_time={start_time}&end_time={end_time}"
            )
            return redirect(url)
        else:
            return redirect('home')

    if (
        request.GET.get('date')
        and request.GET.get('start_time')
        and request.GET.get('end_time')
    ):
        date = request.GET.get('date')
        start_time = request.GET.get('start_time')
        end_time = request.GET.get('end_time')
    else:
        now = datetime.now()
        date = now.date().isoformat()
        start_time = now.strftime('%H:%M')
        end_time = (now + timedelta(hours=1)).strftime('%H:%M')

    check_bookings_form = CheckBookingsForm(initial={
        'date': date,
        'start_time': start_time,
        'end_time': end_time,
    })

    # Exclude workspaces with overlapping bookings
    available_workspaces = WorkSpace.objects.exclude(
        bookings__booking_date=date,
        bookings__start_time__lt=end_time,
        bookings__end_time__gt=start_time,
    )

    booking_form = BookingForm()

    workspaces = WorkSpace.objects.all()

    user_editable_workspaces = WorkSpace.objects.filter(
        bookings__user=request.user,
        bookings__booking_date=date,
        bookings__start_time__lt=end_time,
        bookings__end_time__gt=start_time,
    ).distinct()

    user_bookings = Booking.objects.filter(
        user=request.user,
        workspace__in=[ws.id for ws in workspaces],
        booking_date=date,
        start_time__lt=end_time,
        end_time__gt=start_time,
    )
    workspace_to_user_booking_id = {
        b.workspace_id: b.id
        for b in user_bookings
    }

    return render(
        request=request,

        context={
            "booking_form": booking_form,
            "check_bookings_form": check_bookings_form,
            "workspaces": workspaces,
            "available_workspaces": available_workspaces,
            "user_editable_workspaces": user_editable_workspaces,
            "workspace_to_booking_id": workspace_to_user_booking_id,
        },
        template_name="booking/interactive_floorplan.html",
    )


def workspace_list(request):
    workspaces = WorkSpace.objects.all()
    return render(
        request,
        'booking/workspace_list.html',
        {'workspaces': workspaces}
    )


@login_required
def create_booking(request):
    """
    Create a new booking related to :model:`Booking`
    """
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.status = "confirmed"
            booking.save()

            date = booking_form.cleaned_data['booking_date']
            start_time = booking_form.cleaned_data['start_time']
            end_time = booking_form.cleaned_data['end_time']

            messages.add_message(
                request,
                messages.SUCCESS,
                "Booking confirmed",
            )
            url = (
                reverse('book_workspace')
                + f"?date={date}&start_time={start_time}&end_time={end_time}"
            )
            return redirect(url)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Booking could not be made. Select a different slot",
            )
    return redirect('book_workspace')


@login_required
def update_booking(request, booking_id):
    """
    Update an existing booking related to :model:`Booking`
    Supports AJAX POST requests
    Return JSON response
    """
    if request.method == "POST":
        try:
            booking = Booking.objects.get(
                pk=booking_id,
                user=request.user,
            )
            booking_form = BookingForm(
                data=request.POST,
                instance=booking,
            )

            if booking_form.is_valid():
                booking = booking_form.save(commit=False)
                booking.status = "confirmed"
                booking.save()
                return JsonResponse({
                    'success': True,
                    'message': 'Booking updated.'
                })
            else:
                # log errors for debugging
                print("BookingForm errors:", booking_form.errors)  

                json_errors = {}
                for field, err_list in booking_form.errors.get_json_data().items():
                    json_errors[field] = [e.get('message') for e in err_list]

                # return structured errors to the client for display
                return JsonResponse(
                    {
                        'success': False,
                        'message': 'Not updated - Errors in submitted booking form',
                        'errors': json_errors,
                        'non_field_errors': list(booking_form.non_field_errors()),
                    },
                    status=400
                )
        except Exception as e:
            return JsonResponse(
                {
                    'success': False,
                    'message': f'Error: {str(e)}'
                },
                status=500
            )

        pass
    else:
        return JsonResponse(
                {
                    'success': False,
                    'message': 'Unsupported request.'
                },
                status=405
            )


@login_required
def cancel_booking(request, booking_id):
    """
    Update an existing booking related to :model:`Booking`
    Supports requests
    Return JSON response
    """
    print("Cancelling")
    try:
        booking = Booking.objects.get(
            pk=booking_id,
            user=request.user,
        )

        booking.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Booking cancelled"
        )
    except Exception as e:
        messages.add_message(
            request,
            messages.ERROR,
            f"Error cancelling booking - {e}"
        )

    # AJAX support
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"success": True, "message": "Complete"})

    if request.GET.get('from') == 'workspace':
        return redirect('book_workspace')
    else:
        return redirect('my_bookings')


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

@login_required
def edit_booking_form(request, booking_id):
    booking = Booking.objects.get(pk=booking_id, user=request.user)
    form = BookingForm(instance=booking)
    return render(request, 'booking/edit_booking_form.html', {'form': form, 'booking': booking})


def get_workspace_details(request, workspace_id):
    """
    Returns JSON response related to :model:`Workspace`
    """
    try:
        workspace = WorkSpace.objects.get(pk=workspace_id)
        data = {
            "id": workspace.id,
            "name": workspace.name,
            "location": workspace.location,
            "capacity": workspace.capacity,
            "workspace_type": workspace.get_workspace_type_display(),
            "description": workspace.description,
            "amenities": workspace.get_amenities_list(),
            "status": workspace.status,
        }
        return JsonResponse({
            "success": True,
            "workspace": data
        })
    except WorkSpace.DoesNotExist:
        return JsonResponse({
            "success": False,
            "error": "Workspace not found"
        }, status=404)


@login_required
def get_booking_details(request, booking_id):
    """
    Returns JSON response related to :model:`Booking`
    """
    try:
        booking = Booking.objects.select_related(
            'workspace', 'user'
        ).get(
            pk=booking_id,
            user=request.user
        )
        data = {
            "id": booking.id,
            "workspace_id": booking.workspace.id,
            "workspace_name": booking.workspace.name,
            "booking_date": booking.booking_date.isoformat(),
            "start_time": booking.start_time.strftime('%H:%M'),
            "end_time": booking.end_time.strftime('%H:%M'),
            "status": booking.status,
            "purpose": booking.purpose,
            "notes": booking.notes,
        }
        return JsonResponse({
            "success": True,
            "booking": data
        })
    except Booking.DoesNotExist:
        return JsonResponse({
            "success": False,
            "error": "Booking not found"
        }, status=404)
