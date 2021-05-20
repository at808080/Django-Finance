from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #assign a one to one relatinoship with django's existing user model

    image = models.ImageField(default='default.jpg', upload_to='profile_pictures') #default image is a manually added static file in the media/profile_pictures directory

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        ii = Image.open(self.image.path) #restricting profile images to a 240x240 size
        if ii.width > 240 or ii.height > 240:
            output_size = (240, 240)
            ii.save(self.image.path)
