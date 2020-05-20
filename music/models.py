from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

CATEGOTY_CHOICES = (
    ('pop', 'POP'),
    ('electronic', 'ELECTRONIC'),
    ('bollywood_romantic', 'BOLLYWOOD ROMANTIC'),
    ('bollywood_singles', 'BOLLYWOOD SINGLES'),
    ('country', 'COUNTRY'),
    ('animated', 'ANIMATED MUSIC VIDEO'),
)

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('hindi', 'HINDI'),
    ('japanese', 'JAPANESE'),
)

class Music(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000)
    image = models.ImageField(upload_to = 'music')
    og_singer = models.CharField(max_length = 100)
    singer = models.CharField(max_length = 100)
    category = models.CharField(choices = CATEGOTY_CHOICES, max_length = 40)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length = 10)
    year_of_release = models.DateField()
    popularity_count = models.IntegerField(default = 0)
    rating = models.IntegerField(default=0)
    slug = models.SlugField(blank = True, null = True)
    music_video = models.URLField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Music, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

LINK_CHOICES = (
    ('D', 'DOWNLOAD'),
    ('W', 'WATCH'),
)

class MusicLink(models.Model):
    music = models.ForeignKey(Music, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(max_length = 1, choices = LINK_CHOICES)
    link = models.URLField(default='WATCH')

    def __str__(self):
        return str(self.music)
