from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    def post_detail(self):
            return reverse('book_detail', args=[str(self.id)])
         
    BOOKING_CHOICES = [('In Library', '館藏中'),('Reserverd','預約中'),('On load','外借中')]

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    date = models.CharField(max_length=200)
    img = models.TextField()
    booking = booking = models.CharField(max_length=20, choices=BOOKING_CHOICES, default='In Library')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.title

class Post2(models.Model):
    def post_detail(self):
        return reverse('book_detail', args=[str(self.id)])
    
    BOOKING_CHOICES = [('In Library', '館藏中'),('Reserverd','預約中'),('On load','外借中')]

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    date = models.CharField(max_length=200)
    img = models.TextField()
    booking = booking = models.CharField(max_length=20, choices=BOOKING_CHOICES, default='In Library')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

        