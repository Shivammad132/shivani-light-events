from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('packages/', views.packages, name='packages'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('booking/', views.booking, name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path("support/", views.support, name="support"),
    
]
