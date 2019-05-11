from django.db import models
from django.conf import settings
from profiles.models import Profile
# Create your models here.



class Feedback(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    detail = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    complain = models.BooleanField(default=False)
    happy = models.BooleanField(default=True)








