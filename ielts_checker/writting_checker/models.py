from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class UserWrittings(models.Model):
    user_name = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    task = models.CharField(max_length=500)
    writting = RichTextField()
    score = models.FloatField()
    feed_back = models.TextField()
    date = models.DateField(auto_now_add=True)
    public_status = models.BooleanField(default=False)