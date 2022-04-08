from django.db import models

# Create your models here.

class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.first_name

class Shift(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    workers = models.ManyToManyField(Worker, blank=True)

    def __str__(self) -> str:
        return self.name