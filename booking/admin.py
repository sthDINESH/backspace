from django.contrib import admin
from .models import WorkSpace, Booking

admin.site.register(WorkSpace)
# admin.site.register(Booking)


@admin.register(Booking)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'workspace', 'booking_date', 'start_time', 'end_time', 'status')
    list_filter = ('user', 'booking_date', 'status')
