# Generated by Django 2.2.5 on 2019-09-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_list_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='item_image',
            new_name='item1_image',
        ),
        migrations.AddField(
            model_name='list',
            name='item2_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='list',
            name='item3_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]
