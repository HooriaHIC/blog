# Generated by Django 2.2.5 on 2019-09-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190909_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_pics'),
        ),
    ]
