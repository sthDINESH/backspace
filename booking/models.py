from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Booking, StudySpace
from .forms import BookingForm


# ==================== EXISTING HOME VIEW ====================

def home(request):
    """Homepage view - with the existing code."""
    return render(
        request=request,
        template_name="booking/home.html",
    )


# ==================== BOOKING LIST VIEW (READ) ====================

@login_required
def booking_list(request):
    """
    Display all bookings for the logged-in user.
    Separates upcoming and past bookings.
    
    US-007: View My Bookings (Epic 3 - READ)
    LO2.2: CRUD Functionality
    """
    now = timezone.now()
    today = now.date()
    current_time = now.time()
    
    # Get all bookings for the current user
    all_bookings = Booking.objects.filter(user=request.user)
    
    # Separate upcoming and past bookings
    upcoming_bookings = all_bookings.filter(
        Q(booking_date__gt=today) |
        Q(booking_date=today, end_time__gte=current_time)
    ).filter(status__in=['pending', 'confirmed']).order_by('booking_date', 'start_time')
    
    past_bookings = all_bookings.filter(
        Q(booking_date__lt=today) |
        Q(booking_date=today, end_time__lt=current_time) |
        Q(status__in=['cancelled', 'completed'])
    ).order_by('-booking_date', '-start_time')
    
    context = {
        'upcoming_bookings': upcoming_bookings,
        'past_bookings': past_bookings,
        'total_bookings': all_bookings.count(),
    }
    
    return render(request, 'booking/booking_list.html', context)


# ==================== CREATE BOOKING (CREATE) ====================

@login_required
def booking_create(request):
    """
    Create a new booking.
    
    US-006: Create New Booking (Epic 3 - CREATE)
    LO2.2: CRUD Functionality
    LO2.4: Forms and Validation
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = 'confirmed'
            
            try:
                booking.save()
                messages.success(
                    request,
                    f'Booking created successfully! {booking.study_space.name} on {booking.booking_date} from {booking.start_time.strftime("%H:%M")} to {booking.end_time.strftime("%H:%M")}.'
                )
                return redirect('booking_list')
            except Exception as e:
                messages.error(request, f'Error creating booking: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        study_space_id = request.GET.get('study_space')
        initial_data = {}
        
        if study_space_id:
            try:
                study_space = StudySpace.objects.get(pk=study_space_id)
                initial_data['study_space'] = study_space
            except StudySpace.DoesNotExist:
                pass
        
        form = BookingForm(initial=initial_data)
    
    available_spaces = StudySpace.objects.filter(status='available')
    
    context = {
        'form': form,
        'available_spaces': available_spaces,
        'page_title': 'Create New Booking',
    }
    
    return render(request, 'booking/booking_form.html', context)





