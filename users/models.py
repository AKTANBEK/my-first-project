from django.contrib.auth.models import User
from django.db import models


class UserCreate(User):
    STATUS_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='student')

