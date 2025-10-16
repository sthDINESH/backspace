from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, time


# ============================================================================
# WORKSPACE MODEL
# ============================================================================
# Represents physical workspaces (desks, meeting rooms, booths, etc.)
# Links to SVG floor plan for visual selection
# Tracks availability status for booking logic
# ============================================================================

class WorkSpace(models.Model):

    # ========================================================================
    # CHOICES - Define dropdown options for certain fields
    # ========================================================================

    WORKSPACE_TYPES = [
        ('desk', 'Hot Desk'),
        ('meeting', 'Meeting Room'),
        ('booth', 'Private Booth'),
        ('pod', 'Collaboration Pod'),
    ]

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('maintenance', 'Under Maintenance'),
        ('unavailable', 'Unavailable'),
    ]

    SHAPE_CHOICES = [
        ('rect', 'Rectangle'),
    ]

    # ========================================================================
    # BASIC INFORMATION FIELDS
    # ========================================================================

    name = models.CharField(
        max_length=100,
        unique=True,  # Enhanced: Prevents duplicate workspace names
        help_text="Unique name for the workspace (e.g., 'Desk-A1', 'Meeting Room 2')"
    )

    location = models.CharField(
        max_length=255,
        help_text="Physical location or floor level (e.g., 'Ground Floor', 'First Floor East Wing')"
    )

    capacity = models.PositiveIntegerField(
        help_text="Maximum number of people this space can accommodate"
    )

    workspace_type = models.CharField(
        max_length=20,
        choices=WORKSPACE_TYPES,
        default='desk',
        help_text="Type of workspace for filtering and categorisation"
    )

    description = models.TextField(
        blank=True,
        help_text="Detailed description of the workspace"
    )

    # ========================================================================
    # FLOOR PLAN INTEGRATION FIELDS
    # ========================================================================

    svg_id = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique ID matching the SVG element in the floor plan (e.g., 'desk-a1-svg')"
    )

    svg_shape = models.CharField(
        choices=SHAPE_CHOICES,
    )

    svg_x_coord = models.PositiveIntegerField(
        help_text="x-coordinate for the workspace location"
    )

    svg_y_coord = models.PositiveIntegerField(
        help_text="y-coordinate for the workspace location"
    )

    svg_width = models.PositiveIntegerField(
        help_text="Width of the workspace"
    )

    svg_height = models.PositiveIntegerField(
        help_text="Height of the workspace"
    )

    # ========================================================================
    # AVAILABILITY & STATUS FIELDS
    # ========================================================================

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available',
        help_text="Current status - controls whether workspace can be booked"
    )

    # ========================================================================
    # ADDITIONAL FEATURES
    # ========================================================================

    amenities = models.TextField(
        blank=True,
        help_text="Comma-separated list of amenities (e.g., 'WiFi, Monitor, Whiteboard')"
    )

    hourly_rate = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.00,
        help_text="Hourly rate for booking (£0.00 for free spaces)"
    )

    # ========================================================================
    # METADATA FIELDS
    # Automatic timestamps for tracking when records are created/updated
    # ========================================================================

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ========================================================================
    # META CLASS
    # Configure how Django handles this model
    # ========================================================================

    class Meta:
        ordering = ['workspace_type', 'name']  # Default sort order
        verbose_name = 'Workspace'
        verbose_name_plural = 'Workspaces'

    # ========================================================================
    # STRING REPRESENTATION
    # How the model appears in admin and debugging
    # ========================================================================

    def __str__(self):
        return self.name

    # ========================================================================
    # HELPER METHODS
    # Utility functions for common operations
    # ========================================================================

    def get_amenities_list(self):
        """
        Returns amenities as a Python list for easy template display.

        Example: "WiFi, Monitor, Whiteboard" → ['WiFi', 'Monitor', 'Whiteboard']
        """
        if self.amenities:
            return [amenity.strip() for amenity in self.amenities.split(',')]
        return []

    def is_available(self):
        """
        Check if the workspace is currently available for booking.

        Returns:
            bool: True if status is 'available', False otherwise
        """
        return self.status == 'available'

    def get_display_name(self):
        """
        Get formatted display name with workspace type.

        Example: "Desk-A1 (Hot Desk)"
        """
        return f"{self.name} ({self.get_workspace_type_display()})"


# ============================================================================
# BOOKING MODEL
# ============================================================================
# Represents user reservations for workspaces
# Handles all booking logic, validation, and conflict checking
# Links User ← Booking → WorkSpace
# ============================================================================

class Booking(models.Model):
    """
    Represents a booking/reservation made by a user for a specific workspace.

    Core functionality for Epic 3 (CRUD Operations):
    - Create: Users can make new bookings
    - Read: Users can view their bookings
    - Update: Users can edit existing bookings
    - Delete: Users can cancel bookings

    """

    # ========================================================================
    # CHOICES - Booking status options
    # ========================================================================

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    # ========================================================================
    # FOREIGN KEY RELATIONSHIPS
    # Links this booking to a User and a WorkSpace
    # ========================================================================

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # If user deleted, delete their bookings
        related_name='bookings',   # Allows: user.bookings.all()
        help_text="User who made the booking"
    )

    workspace = models.ForeignKey(
        WorkSpace,
        on_delete=models.CASCADE,  # If workspace deleted, delete its bookings
        related_name='bookings',   # Allows: workspace.bookings.all()
        help_text="Workspace being booked"
    )

    # ========================================================================
    # BOOKING DATE & TIME FIELDS
    # When the booking is scheduled
    # ========================================================================

    booking_date = models.DateField(
        help_text="Date of the booking"
    )

    start_time = models.TimeField(
        help_text="Start time of the booking"
    )

    end_time = models.TimeField(
        help_text="End time of the booking"
    )

    # ========================================================================
    # STATUS & ADDITIONAL INFORMATION
    # ========================================================================

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='confirmed',
        help_text="Current status of the booking"
    )

    purpose = models.CharField(
        max_length=200,
        blank=True,
        help_text="Purpose of the booking (optional)"
    )

    notes = models.TextField(
        blank=True,
        help_text="Additional notes or special requirements"
    )

    # ========================================================================
    # METADATA FIELDS
    # Automatic timestamps
    # ========================================================================

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ========================================================================
    # META CLASS
    # Configure model behavior and database constraints
    # ========================================================================

    class Meta:
        ordering = ['-booking_date', '-start_time']  # Newest bookings first
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

        # Database constraint: Ensure end_time is always after start_time
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_time__gt=models.F('start_time')),
                name='end_time_after_start_time'
            )
        ]

    # ========================================================================
    # STRING REPRESENTATION
    # ========================================================================

    def __str__(self):
        return f"{self.user.username} - {self.workspace.name} on {self.booking_date}"

    # ========================================================================
    # VALIDATION METHOD
    # Runs before saving to check business rules
    # ========================================================================

    def clean(self):
        """
        Validate the booking before saving.

        Checks:
        - Booking date is not in the past
        - End time is after start time
        - Times are within business hours (8 AM - 10 PM)
        - Workspace is available
        - No overlapping bookings for the same workspace

        Raises:
            ValidationError: If any validation check fails
        """
        errors = {}

        # --------------------------------------------------------------------
        # CHECK 1: Booking date must not be in the past
        # --------------------------------------------------------------------
        if self.booking_date and self.booking_date < timezone.now().date():
            errors['booking_date'] = "Booking date cannot be in the past."

        # --------------------------------------------------------------------
        # CHECK 2: End time must be after start time
        # --------------------------------------------------------------------
        if self.start_time and self.end_time:
            if self.end_time <= self.start_time:
                errors['end_time'] = "End time must be after start time."

            # ----------------------------------------------------------------
            # CHECK 3: Booking must be within business hours
            # Business hours: 8:00 AM to 10:00 PM
            # ----------------------------------------------------------------
            business_start = time(8, 0)
            business_end = time(22, 0)

            if self.start_time < business_start or self.end_time > business_end:
                errors['start_time'] = "Bookings must be between 8:00 AM and 10:00 PM."

        # --------------------------------------------------------------------
        # CHECK 4: Workspace must be available
        # --------------------------------------------------------------------
        if self.workspace and not self.workspace.is_available():
            errors['workspace'] = f"This workspace is currently {self.workspace.status}."

        # --------------------------------------------------------------------
        # CHECK 5: No overlapping bookings
        # Prevent double-booking the same workspace at the same time
        # --------------------------------------------------------------------
        if self.workspace and self.booking_date and self.start_time and self.end_time:
            # Find all confirmed/pending bookings for this workspace on this date
            overlapping_bookings = Booking.objects.filter(
                workspace=self.workspace,
                booking_date=self.booking_date,
                status__in=['pending', 'confirmed']
            ).exclude(pk=self.pk)  # Exclude current booking (for updates)

            # Check each booking for time overlap
            for booking in overlapping_bookings:
                # Overlap logic: (start1 < end2) AND (end1 > start2)
                if (
                    self.start_time < booking.end_time
                    and self.end_time > booking.start_time
                ):
                    errors['start_time'] = (
                        f"This time slot conflicts with an existing booking "
                        f"({booking.start_time} - {booking.end_time})."
                    )
                    break

        # Raise all validation errors at once
        if errors:
            raise ValidationError(errors)

    # ========================================================================
    # SAVE METHOD OVERRIDE
    # Ensure validation runs before every save
    # ========================================================================

    def save(self, *args, **kwargs):
        """
        Override save to run validation automatically.
        This ensures clean() is always called before saving.
        """
        self.full_clean()  # Run all validation
        super().save(*args, **kwargs)  # Call parent save method

    # ========================================================================
    # HELPER METHODS
    # Utility functions for common booking operations
    # ========================================================================

    def get_duration(self):
        """
        Calculate the duration of the booking in hours.

        Returns:
            float: Duration in hours (e.g., 2.5 for 2 hours 30 minutes)
        """
        if self.start_time and self.end_time:
            start_datetime = datetime.combine(self.booking_date, self.start_time)
            end_datetime = datetime.combine(self.booking_date, self.end_time)
            duration = end_datetime - start_datetime
            return duration.total_seconds() / 3600  # Convert seconds to hours
        return 0

    def is_past(self):
        """
        Check if the booking is in the past.

        Returns:
            bool: True if booking end time has passed, False otherwise
        """
        booking_datetime = datetime.combine(self.booking_date, self.end_time)
        return timezone.make_aware(booking_datetime) < timezone.now()

    def can_be_modified(self):
        """
        Check if the booking can still be edited or cancelled.

        A booking can be modified if:
        - It's not in the past
        - Status is not 'cancelled' or 'completed'

        Returns:
            bool: True if booking can be modified, False otherwise
        """
        return (
            not self.is_past()
            and self.status not in ['cancelled', 'completed']
        )

    def cancel(self):
        """
        Cancel the booking by changing its status to 'cancelled'.

        Returns:
            bool: True if successfully cancelled, False if can't be modified
        """
        if self.can_be_modified():
            self.status = 'cancelled'
            self.save()
            return True
        return False