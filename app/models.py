from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='profile_images')
    address = models.CharField(max_length=500)
    type = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.username