# Generated by Django 3.0.3 on 2020-05-16 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20200516_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='og_singer',
            field=models.CharField(max_length=100),
        ),
    ]
