from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    duration = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title