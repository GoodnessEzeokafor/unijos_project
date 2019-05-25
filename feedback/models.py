from django.db import models
from django.conf import settings
from profiles.models import Profile
# Create your models here.



class Feedback(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30, help_text='Feedback Topic')
    email = models.EmailField(help_text='Enter Your Email')
    detail = models.TextField(blank=True, null=True, verbose_name='Text', help_text='Enter Message')
    date = models.DateTimeField(auto_now_add=True)
    complain = models.BooleanField(default=False)
    happy = models.BooleanField(default=True)




    class Meta:
        db_table  = "at_feedbacks"




