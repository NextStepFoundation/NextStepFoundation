from django.db import models
from django.utils import timezone

# Create your models here.


class Link(models.Model):
    linkvisa = models.CharField(max_length=100, null=True, blank=True)
