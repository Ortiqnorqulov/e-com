from django.core.validators import FileExtensionValidator
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User


################################################################################################################
################################################################################################################
################################################################################################################
from user.models import Client


class Blog(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/Blog',

    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Blog)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Blog.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


################################################################################################################
################################################################################################################
################################################################################################################


class Comment_blog(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, blank=True)
    email = models.CharField(blank=True, max_length=50)
    comment = models.TextField(max_length=255,blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
