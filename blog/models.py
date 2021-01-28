from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE, default='Unknown')
    pub_date = models.DateTimeField('date published', default=timezone.now)
    title = models.CharField(max_length=200)
    body = models.TextField()

    class Meta:
        ordering = ['-pub_date']

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
