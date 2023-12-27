from django.db import models
from PIL import Image
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from hotelmanagement.settings import AUTH_USER_MODEL


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email address", max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    join_date = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    nid = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=11, null=True)
    division = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    upazila = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='profile_image/', default='no-image.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_password_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.email} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ReportIssue(models.Model):
    REASON_CHOICES = [
        (1, 'Reception wasn’t good'),
        (2, 'Booked Accidentally'),
        (3, 'Don\'t want to Book'),
    ]
    
    reason = models.IntegerField(choices=REASON_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.get_reason_display()
    
class Ticket(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    ISSUE_CHOICES = [
        ('lost_luggages', 'Lost Luggages'),
        ('lost_tickets', 'Lost Tickets'),
        ('lost_profile', 'Lost Profile'),
    ]

    DEPARTMENT_CHOICES = [
        ('baggage_luggages', 'Baggage & Luggages'),
        ('support_tickets', 'Support Tickets'),
        ('baggage_luggages', 'Baggage & Luggages'),
    ]

    PRIORITY_CHOICES = [
        ('normal', 'Normal'),
        ('medium', 'Medium'),
        ('difficult', 'Difficult'),
    ]
    
    issue = models.CharField(max_length=255, choices=ISSUE_CHOICES)
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)
    priority = models.CharField(max_length=255, choices=PRIORITY_CHOICES)
    message = models.TextField()
    
    def __str__(self):
        return self.get_issue_display()
    
