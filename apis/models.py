from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField()
    time = models.DateTimeField()