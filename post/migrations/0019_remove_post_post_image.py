# Generated by Django 3.0.5 on 2020-05-16 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_auto_20200516_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
    ]
