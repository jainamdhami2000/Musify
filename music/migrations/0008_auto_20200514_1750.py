# Generated by Django 3.0.3 on 2020-05-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20200514_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='category',
            field=models.CharField(choices=[('rock', 'ROCK'), ('pop', 'POP'), ('electronic', 'ELECTRONIC'), ('bollywood_romantic', 'BOLLYWOOD ROMANTIC'), ('bollywood_singles', 'BOLLYWOOD SINGLES'), ('country', 'COUNTRY'), ('animated', 'ANIMATED MUSIC VIDEO')], max_length=40),
        ),
    ]
