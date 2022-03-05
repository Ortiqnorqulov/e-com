from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# - - - - - - - - - - - - - - - CREATOR / ADMIN - - - - - - - - - - - - - - - #

class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(upload_to='images/Admin', validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    def __str__(self):
        return self.user.username

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()





class Client(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True,null=True)
    address = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True,max_length=25)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/Clients', validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')

    def __str__(self):
        return self.user.username

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


# - - - - - - - - - - - - - - - BRANDS- - - - - - - - - - - - - - - #
class Brands(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/Brands',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
