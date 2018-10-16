from django.db import models
from django.contrib.auth.models import Permission,User
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    # artist is a column name in another database
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    '''def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})
    '''

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
      return self.song_title