import uuid
# import os
from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


# Upload Paths

def get_image_path(instance, filename):
    return "user_{}/{}".format(instance, instance.id)

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    interests = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=40, null=True, blank=True)
    date_profile_created = models.DateTimeField(auto_now_add=True)
    date_profile_updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to=get_image_path)
 

    # Methods

    def __str__(self):
        '''
        Returns The String Representation Of The Profile Model
        '''
        return '{} {}'.format(self.first_name, self.last_name)
        


