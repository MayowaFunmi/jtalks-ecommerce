from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
#from courses.models import Courses


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='admin_pics/%Y/%m/%d/', null=True, blank=True)
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(choices=GENDER, max_length=10, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    
    Here_about_us = [
        ('WhatsApp', 'WhatsApp'),
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('YouTube', 'YouTube'),
        ('Blog', 'Blog')
    ]
    about_us = models.CharField(choices=Here_about_us, max_length=20, null=True, blank=True)
    referral = models.CharField(max_length=50, help_text="Enter your referral name, leave blank if none", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    # USERNAME_FIELD = "email"

    # REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# @receiver(post_save, sender=User)
# def created_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
    

# Users Library moved to Courses model
