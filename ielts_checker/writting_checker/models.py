from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserWrittings(models.Model):
    user_name = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    task = models.CharField(max_length=200)
    writting = models.TextField()
    score = models.FloatField()
    feed_back = models.TextField()
    date = models.DateField(auto_now_add=True)