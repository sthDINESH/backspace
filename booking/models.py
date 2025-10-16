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

