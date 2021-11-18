from django.db import models
from django.utils import timezone

# Create your models here.


class Messages(models.Model):
    date_sent = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=300)

    class Meta:
        ordering = ("-date_sent",)

    def __str__(self):
        return self.name
