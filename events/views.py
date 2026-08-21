from django.shortcuts import render, redirect
from .models import (Service, Package, Booking, GalleryImage, Testimonial, SupportRequest)
from .forms import SupportRequestForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'events/home.html')

def services(request):
    services = Service.objects.filter(
        is_active=True
    )
    return render(request, 'events/services.html', {'services': services})

def packages(request):
    packages = Package.objects.filter(
        is_active=True
    )
    return render(request, 'events/packages.html', {'packages': packages})

def gallery(request):
    gallery_images = GalleryImage.objects.filter(
        is_active=True
    )
    return render(request, 'events/gallery.html', {'gallery_images': gallery_images})

def testimonials(request):
    testimonials = Testimonial.objects.filter(
        is_active=True
    ).order_by('-created_at')

    return render(request, 'events/testimonials.html', {'testimonials': testimonials})

def about(request):
    return render(request, 'events/about.html')

def booking(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        event_type = request.POST.get('event_type')
        event_date = request.POST.get('event_date')
        location = request.POST.get('location')
        requirements = request.POST.get('requirements')

        # Save booking in database
        Booking.objects.create(
            name=name,
            phone=phone,
            event_type=event_type,
            event_date=event_date,
            location=location,
            requirements=requirements,
        )

        # Send booking notification email
        send_mail(
            subject='New Event Booking - Shivani Lights & Events',

            message=f"""
New Event Booking Received

Customer Name: {name}
Mobile Number: {phone}
Event Type: {event_type}
Event Date: {event_date}
Venue / Location: {location}

Requirements:
{requirements}

Please contact the customer for further discussion.

Shivani Lights & Events
""",

            from_email=settings.EMAIL_HOST_USER,

            recipient_list=[settings.EMAIL_HOST_USER],

            fail_silently=False,
        )

        return redirect('booking_success')

    return render(request, 'events/booking.html')

def booking_success(request):
    return render(request, 'events/booking_success.html')

def support(request):

    if request.method == "POST":
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("support_success")
    else:
        form = SupportRequestForm()
    return render(
        request,
        "events/support.html",
        {
            "form": form
        }
    )