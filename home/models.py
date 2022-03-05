from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from user.models import Client
from product.models import Product
from django.contrib.auth.models import User


################################################################################################################
################################################################################################################
################################################################################################################


class Informations(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(blank=True, max_length=20)
    email = models.CharField(max_length=255, blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    location = models.CharField(max_length=500)
    logo = models.ImageField(blank=True, upload_to='images/logo',
                             validators=[FileExtensionValidator(allowed_extensions=['svg', 'jpg'])])
    icon = models.ImageField(blank=True, upload_to='images/icon',
                             validators=[FileExtensionValidator(allowed_extensions=['svg', 'jpg'])])
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


@receiver(pre_save, sender=Informations)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Informations.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


################################################################################################################
################################################################################################################
################################################################################################################


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    subject = models.TextField(blank=True, max_length=255)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


################################################################################################################
################################################################################################################
################################################################################################################


class Aboutus(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/Aboutus',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


@receiver(pre_save, sender=Aboutus)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Aboutus.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


################################################################################################################
################################################################################################################
################################################################################################################


class Faq(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Yopilgan'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=1000)
    answer = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


################################################################################################################
################################################################################################################
################################################################################################################


class NewsLatter(models.Model):
    email = models.CharField(max_length=255)
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


################################################################################################################
################################################################################################################
################################################################################################################


class Slider(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/Slider',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


@receiver(pre_save, sender=Slider)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Slider.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


################################################################################################################
################################################################################################################
################################################################################################################

class Wishlist(models.Model):
    user = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.product.title


class Adversiting(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/Slider',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
