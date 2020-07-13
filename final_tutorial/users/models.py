from django.db import models

GROUP_CHOICES = (
    ('SA', 'Super Admin'),
    ('AD', 'Admin'),
    ('US', 'User')
)

STATUS_CHOICES = (
    ('AC', 'Active'),
    ('SU', 'Suspended'),
    ('NV', 'Not Verified')
)

# Create your models here.
class User(models.Model):
    username = models.CharField(blank=False, max_length=50, unique=True)
    password = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    group = models.CharField(max_length=2, choices=GROUP_CHOICES, default='US')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AC')