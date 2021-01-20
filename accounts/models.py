from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass


class Team(models.Model):
    name = models.CharField(max_length=64)
    position = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    image = models.ImageField(upload_to='blog')

    def __str__(self):
        return self.name


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=64)
    data_filter = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Portfolio categories'

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    category = models.ManyToManyField(PortfolioCategory, related_name='portfolio')
    active = models.BooleanField(default=True)
    description = models.TextField()
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='portfolio')

    def __str__(self):
        return f"{self.portfolio} - {self.image}"


class Blog(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    show_image = models.BooleanField(default=True)
    video = models.TextField(blank=True, null=True)
    show_video = models.BooleanField(default=True)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
