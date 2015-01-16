from django.db import models
from datetime import date

# Create your models here.
class Article(models.Model):
    """

    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateField(default=date.today())
    
    likes = models.IntegerField()

    def __str__(self):
        return self.title
