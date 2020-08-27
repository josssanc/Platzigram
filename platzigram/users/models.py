"""Users Models"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """Profile Model Proxy Model extends from the base data with other information"""
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    website = models.CharField(max_length=200,blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=28, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
        )

    creted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

def __str__(self):
    """Return Username"""
    return self.user.username

