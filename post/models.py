from django.db import models

# Create your models here.



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}{1}/{2}'.format(instance.user.profile,instance.user.id, filename)


class Post(models.Model):
    title = models.CharField(
        max_length = 255, 
        null = False, 
        blank = False
    )
    description = models.TextField()
    file_upload = models.FileField(upload_to = user_directory_path)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


