from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    cover_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title