import uuid
# import os
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
# Create your models here.


# Upload Paths

def get_image_path(instance, filename):
    return "user_{}/{}".format(instance, instance.profile_id)

class Profile(models.Model):
    '''

    Model : Profile

    Fields:
        - id
        - user
        - first_name
        - last_name
        - level
        - interests
        - department
        - date_profile_created
        - date_profile_updated

    Methods: 
        def __str__(self):
            """ 
                Returns The String Representation Of The Profile which is the first_name and last_name
            """
            return '{} {}'.format(self.first_name, self.last_name)

    Description:
        This is the table responsible for createting profile for users
        It has a one to one field relationship with the user table
    

    Created: th May 2019
    Developer: Goodness Ezeokafor
    '''

    LEVEL_CHOICE = (
        ('100lvl', '100 LEVEL'),
        ('200lvl', '200 LEVEL'),
        ('300lvl', '300 LEVEL'),
        ('400lvl', '400 LEVEL'),
        ('500lvl', '500 LEVEL')
    )
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'user'
    )
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    level = models.CharField(
        max_length=40,
        choices=LEVEL_CHOICE,
        default= '100lvl'
    )
    interests = models.CharField(max_length=255, null=True, blank=True, help_text="Seperated by commas e.t.c Music, Maths, Computers")
    department = models.CharField(max_length=40, null=True, blank=True)
    bio = models.TextField(default='', null=True, blank=True, help_text="Short Bio Of Your Self")
    date_profile_created = models.DateTimeField(auto_now_add=True)
    date_profile_updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to=get_image_path)
 


    class Meta:
        db_table  = "at_profiles"

    # Methods
    def __str__(self):
        '''
        Returns The String Representation Of The Profile Model
        '''
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("profiles:profile_dashboard", args = [self.profile_id])
        

    