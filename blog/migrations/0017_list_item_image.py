# Generated by Django 2.2.5 on 2019-09-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190913_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='item_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]
