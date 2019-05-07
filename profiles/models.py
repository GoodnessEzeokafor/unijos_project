from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    LEVEL_CHOICE = (
        ('100lvl', '100 LEVEL'),
        ('200lvl', '200 LEVEL'),
        ('300lvl', '300 LEVEL'),
        ('400lvl', '400 LEVEL'),
        ('500lvl', '500 LEVEL')
    )
    # DEPT_CHOICE = 
    '''
    User
    First Name
    Last Name
    Dept
    Level
    Interests
    '''
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
    interests = models.CharField(max_length=40, null=True, blank=True)
    depertment = models.CharField(max_length=40, null=True, blank=True)
    # photo = models.ImageField(upload_to='%Y/%m/%d/{}'.format(id))

    # level 

    # def uploaded(self):
    #     return "%Y/%m/%d/{}".format(self.id)


    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

