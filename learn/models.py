from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:30]

    def get_absolute_url(self):
        return reverse('updateBlog', args=[str(self.id)])

    class Meta:
        app_label = 'learn'
