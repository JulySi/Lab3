from django.db import models
from django.utils import timezone


class Note(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    created_date = models.DateTimeField(
        default=timezone.now
    )
    author = models.ForeignKey('auth.User', default=0)
    category = models.ForeignKey('Category', default=0)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
