from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import WorkSpace, Booking
from .forms import BookingForm


def home(request):
    
    booking_form = BookingForm()

    bookings = Booking.objects.filter(
        user=request.user,
    )

    return render(
        request=request,

        context={
            "booking_form": booking_form,
            "bookings": bookings,
        },
        # template_name="booking/home.html",
        template_name="booking/interactive_floorplan.html", 

    )


def workspace_list(request):
    workspaces = WorkSpace.objects.all()
    return render(request, 'booking/workspace_list.html', {'workspaces': workspaces})

# debugging line to check if workspaces are being fetched correctly
# print(WorkSpace.objects.all())


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
                return JsonResponse(
                    {
                        'success': False,
                        'message': (
                            'Not updated - Errors in submitted booking form'
                        )
                    }
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
    try:
        booking = Booking.objects.get(
            pk=booking_id,
            user=request.user,
        )

        booking.delete()
        return JsonResponse({
                'success': True,
                'message': 'Booking cancelled.'
            })
    except Exception as e:
        return JsonResponse(
            {
                'success': False,
                'message': f'Error: {str(e)}'
            },
            status=500
        )

    pass

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

@login_required
def edit_booking_form(request, booking_id):
    booking = Booking.objects.get(pk=booking_id, user=request.user)
    form = BookingForm(instance=booking)
    return render(request, 'booking/edit_booking_form.html', {'form': form, 'booking': booking})

