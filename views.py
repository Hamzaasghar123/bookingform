from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import EventForm, AdminLoginForm, AssignStaffForm
from eventbooking.models import Booking



def booking_submitted(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            cleaned_data = form.cleaned_data
            return render(request, 'eventbooking/BookingSubmitted.html', cleaned_data)
    else:
        form = EventForm()
    return render(request, 'eventbooking/homePage.html', {'form': form})


def home_page(request):
    form = EventForm()
    return render(request, 'eventbooking/homePage.html', {'form': form})


def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('upcoming_bookings')
            else:
                error_message = 'Invalid username or password'
                return render(request, 'eventbooking/adminlogin.html', {'form': form, 'error': error_message})
    else:
        form = AdminLoginForm()
    return render(request, 'eventbooking/adminlogin.html', {'form': form})


def staff_login(request):
    return render(request, 'eventbooking/stafflogin.html')
def upcoming_bookings(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin_login')
    upcoming_events = Booking.objects.all()
    form = AssignStaffForm()
    return render(request, 'eventbooking/upcomingbookings.html', {'upcoming_events': upcoming_events, 'form': form})

def event_details(request, event_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin_login')
    event = get_object_or_404(Booking, id=event_id)
    return render(request, 'eventbooking/event_details.html', {'event': event})

def edit_booking(request, event_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin_login')

    event = get_object_or_404(Booking, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('upcoming_bookings')
    else:
        form = EventForm(instance=event)
    return render(request, 'eventbooking/edit_booking.html', {'form': form, 'event': event})

