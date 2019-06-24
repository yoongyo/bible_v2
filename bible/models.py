from django.db import models


class Bible(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/')
    content = models.TextField()
    mp3 = models.FileField(upload_to='mp3/')
