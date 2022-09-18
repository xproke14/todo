from django.db import models
from categories.models import Category
from django.utils import timezone

class Task(models.Model):
    name = models.CharField(max_length=20)
    done = models.BooleanField(default = False)
    created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # user not needed as they are linked to categories

    def __str__(self):
        return self.name
