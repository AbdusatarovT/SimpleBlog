# Generated by Django 4.1 on 2022-09-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My blog', max_length=250),
        ),
    ]
