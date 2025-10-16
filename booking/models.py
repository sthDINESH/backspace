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



