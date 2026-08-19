from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=10,
        default="ICON"
    )
    description = models.TextField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class Package(models.Model):

    name = models.CharField(
        max_length=100
    )

    price = models.PositiveIntegerField()
    description = models.TextField(
        blank=True
    )
    features = models.TextField(
        help_text="Enter one feature per line."
    )

    popular = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def feature_list(self):
        return [
            feature.strip()
            for feature in self.features.splitlines()
            if feature.strip()
        ]

    def __str__(self):
        return self.name

class GalleryImage(models.Model):

    CATEGORY_CHOICES = [
        ('Wedding', 'Wedding'),
        ('Birthday', 'Birthday'),
        ('Stage', 'Stage'),
        ('Lighting', 'Lighting'),
        ('Haldi', 'Haldi'),
        ('Other', 'Other'),
    ]

    title = models.CharField(
        max_length=100
    )

    image = models.ImageField(
        upload_to='gallery/'
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Other'
    )
    is_active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
class Testimonial(models.Model):

    name = models.CharField(
        max_length=100
    )

    event_type = models.CharField(
        max_length=100
    )

    review = models.TextField()

    rating = models.PositiveSmallIntegerField(
        default=5
    )

    is_active = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Booking(models.Model):

    EVENT_TYPES = [
        ('Wedding', 'Wedding'),
        ('Birthday / Party', 'Birthday / Party'),
        ('Engagement', 'Engagement'),
        ('Haldi / Mehndi', 'Haldi / Mehndi'),
        ('Corporate Event', 'Corporate Event'),
        ('Dulha Rath and Roadlight','Dulha Rath and Roadlight'),
        ('Pickup Rental','Pickup Rental'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPES
    )
    event_date = models.DateField()
    location = models.CharField(
        max_length=200,
        blank=True
    )
    requirements = models.TextField(
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return f"{self.name} - {self.event_type}"


class SupportRequest(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    ]

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField(blank=True, null=True)

    subject = models.CharField(max_length=200)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"