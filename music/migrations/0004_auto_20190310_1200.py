# Generated by Django 2.1.7 on 2019-03-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190309_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
