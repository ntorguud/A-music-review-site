from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField

# Create your models here.
class MusicType(models.Model):
    typename = models.CharField(max_length=255)
    typedescription = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='musictype'

class Song(models.Model):
    songname = models.CharField(max_length=255)
    songtype = models.ForeignKey(MusicType, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered = DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    songurl = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.songname
    
    class Meta:
        db_table='song'

class Review(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Song, on_delete=CASCADE)
    reviewdate = models.DateField()
    review = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table='review'







