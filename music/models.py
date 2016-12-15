from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist_id = models.ForeignKey('Artist', on_delete=models.CASCADE)
    genre_id = models.ForeignKey(
        'Genre', blank=True, null=True, on_delete=models.CASCADE)
    album_icon = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        if self.artist_id:
            return self.title + ' by ' + self.artist_id.name
        return self.title


class Artist(models.Model):
    is_band = models.BooleanField(default=True)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class Song(models.Model):
    file_types = [
        ('mp3', 'mp3'),
        ('wav', 'wav'),
        ('flac', 'flac'),
        ('ogg', 'ogg'),
    ]
    title = models.CharField(max_length=60)
    file_type = models.CharField(
        max_length=7, choices=file_types, default='mp3')
    file = models.BinaryField(blank=True, null=True)
    artist_id = models.ForeignKey('Artist', on_delete=models.CASCADE)
    album_id = models.ForeignKey(
        'Album', blank=True, null=True, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    def toggle_favorite(self):
        if self.is_favorite:
            self.is_favorite = False
        else:
            self.is_favorite = True

    def __unicode__(self):
        if self.artist_id and self.album_id:
            return "%s by %s from the album %s" % (
                self.title, self.artist_id.name, self.album_id.title)
        elif self.artist_id and not self.album_id:
            return "%s by %s" % (self.title, self.artist_id.name)
        else:
            return self.title


class Genre(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name
