from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True)
    publish_datetime = models.DateTimeField()
    category = models.ForeignKey(
        Category,
        related_name='articles',
        on_delete=models.deletion.CASCADE
    )
