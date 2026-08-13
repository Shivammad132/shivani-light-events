from django.contrib import admin
from .models import Service, Package, GalleryImage, Testimonial, Booking, SupportRequest


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'is_active',
        'created_at'
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'title',
        'description',
    )

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):

    list_display = ('name','price','popular','is_active',)
    list_filter = ('popular','is_active',)
    search_fields = ('name',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'is_active',
        'created_at',
    )

    list_filter = ('category','is_active',)

    search_fields = ('title',)
    list_editable = ('is_active',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'event_type',
        'rating',
        'is_active',
        'created_at',
    )

    list_filter = (
        'rating',
        'event_type',
        'is_active',
    )
    search_fields = ('name','review',)
    list_editable = ('rating','is_active',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'event_type',
        'event_date',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'event_type',
        'event_date',
    )

    search_fields = (
        'name',
        'phone',
        'location',
    )

    list_editable = (
        'status',
    )
    readonly_fields = (
        'created_at',
    )

@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "subject",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "phone",
        "email",
        "subject",
    )