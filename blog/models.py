from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

"""
python3 manage.py showmigrations
python3 manage.py makemigrations
python3 manage.py migrate
"""


# Create your models here.
class Post(models.Model):
    class Meta:
        ordering = ('-publish',)

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    # unique_for_dateパラメータはURLを「publishとされた日付+slug」で作る。
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')  # null=True, blank=True
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    def __str__(self):
        return self.title
