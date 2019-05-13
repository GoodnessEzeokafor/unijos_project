from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}{1}/{2}'.format(instance.user.profile,instance.user.id, filename)




STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Posts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_Posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
