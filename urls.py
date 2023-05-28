from django.urls import path
from eventbooking import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('booking_submitted/', views.booking_submitted, name='booking_submitted'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('staff-login/', views.staff_login, name='staff_login'),
    path('upcomingbookings/', views.upcoming_bookings, name='upcoming_bookings'),
    path('event-details/<int:event_id>/', views.event_details, name='event_details'),
    path('edit-booking/<int:event_id>/', views.edit_booking, name='edit_booking'),
]

