# Generated by Django 2.2.5 on 2019-09-10 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190909_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='profile_pics', verbose_name='image'),
        ),
    ]
