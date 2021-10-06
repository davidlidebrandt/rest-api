from django.db import models
from django.db.models.fields import DateField
from django.contrib.auth.models import User

class TestData(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
