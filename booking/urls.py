from django.urls import path
from . import views

urlpatterns = [
    path('workspaces/', views.workspace_list, name='workspace_list'),
    path('booking/create/', views.create_booking, name='create_booking'),
    path(
        'booking/<int:booking_id>/update',
        views.update_booking,
        name='update_booking'
    ),
    path(
        'booking/<int:booking_id>/cancel',
        views.cancel_booking,
        name='cancel_booking'
    ),
    path('', views.home, name='home'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]
