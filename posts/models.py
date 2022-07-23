from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=10000)

    def __str__(self):
        return self.name


class Post(models.Model):
    categories = models.ManyToManyField(Category, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='date', null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='post images/', null=True)
    date = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.author.username} ({self.categories.name})'

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[str(self.id)])

    def get_days(self):
        current = timezone.now()
        delta = current - self.date
        if delta.days <= 1:
            return f'{delta.days} day ago'
        else:
            return f'{delta.days} days ago'


    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('posts:post_list')

class About(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    about_us = models.TextField()
    image_abt = models.ImageField(upload_to="admin_pics", null=True)

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.about_us

class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=250)
    subject = models.CharField(max_length=250, null=True, blank=True)
    message = models.TextField(max_length=1000, help_text='Write Your Message, not more than 1000 characters')

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.full_name