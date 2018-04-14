from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=45)
    content = models.TextField()

    def __str__(self):
        return str(self.title)

