from django.db import models


# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=100),
    last_name = models.CharField(max_length=200),
    age = models.CharField(max_length=2)

    def __init__(self):
        return self.first_name,self.last_name,self.age


class Song(models.Model):
    title = models.CharField(max_length=100),
    date_released = models.DateField(),
    likes = models.CharField(),
    artiste_id = models.ForeignKey(Artiste, default=None)

    def __init__(self):
        return self.title,self.likes,self.artiste_id,self.date_released


class Lyrics(models.Model):
    content = models.TextField(),
    song_id = models.ForeignKey(Song, default=None)
    def __init__(self, content, song_id):
        self.content = content
        self.song_id = song_id

        return content,song_id
