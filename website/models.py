from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(max_length=50, auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)


    def __str__(self):
        return(f"{self.first_name} {self.last_name}")