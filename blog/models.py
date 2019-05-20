from django.db import models
from profiles.models import Profile
import os
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/user_{1}/{2}'.format(instance.profile,instance.profile.profile_id,filename)




class FileUpload(models.Model):
    upload_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date_file_uploaded = models.DateTimeField(auto_now=True)
    date_file_uploaded_updated = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=user_directory_path)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)



    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super(FileUpload, self).delete(*args, **kwargs)
    

    def __str__(self):
        return "{} uploaded by {} on {}".format(self.title, self.profile, self.date_file_uploaded)

    class Meta:
        db_table = "at_file_uploads"
