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
    path('booking/workspace', views.book_workspace, name='book_workspace'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path(
        'booking/workspace/<int:workspace_id>',
        views.get_workspace_details,
        name="workspace_details",
    ),
    path(
        'booking/booking/<int:booking_id>',
        views.get_booking_details,
        name="booking_details",
    ),
    path('booking/<int:booking_id>/edit-form/', views.edit_booking_form, name='edit_booking_form'),
    path('', views.home, name="home"),
]

    