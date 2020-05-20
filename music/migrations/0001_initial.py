# Generated by Django 3.0.3 on 2020-05-13 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='music')),
                ('singer', models.CharField(default='', max_length=100)),
                ('category', models.CharField(choices=[('rock', 'ROCK'), ('pop', 'POP'), ('edm', 'EDM'), ('bollywood', 'BOLLYWOOD')], max_length=10)),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('hindi', 'HINDI')], max_length=10)),
                ('status', models.CharField(choices=[('RR', 'RECENT RELEASES'), ('MP', 'MOST POPULAR'), ('TR', 'TOP RATED')], max_length=2)),
                ('year_of_release', models.DateField()),
                ('popularity_count', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MusicLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'DOWNLOAD'), ('W', 'WATCH')], max_length=1)),
                ('link', models.URLField()),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='music.Music')),
            ],
        ),
    ]
