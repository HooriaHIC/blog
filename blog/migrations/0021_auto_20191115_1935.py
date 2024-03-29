# Generated by Django 2.1 on 2019-11-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20190913_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='item1',
            field=models.CharField(default='item 1', max_length=600),
        ),
        migrations.AlterField(
            model_name='list',
            name='item10',
            field=models.CharField(default='item 10', max_length=600),
        ),
        migrations.AlterField(
            model_name='list',
            name='item2',
            field=models.CharField(default='item 2', max_length=600),
        ),
        migrations.AlterField(
            model_name='list',
            name='item3',
            field=models.CharField(default='item 3', max_length=600),
        ),
        migrations.AlterField(
            model_name='list',
            name='item4',
            field=models.CharField(default='item 4', max_length=600),
        ),
        migrations.AlterField(
            model_name='list',
            name='item5',
            field=models.CharField(default='item 5', max_length=600),
        ),
        migrations.AlterField(
            model_name='list',
            name='item6',
            field=models.CharField(default='item 6', max_length=600),
        ),
        migrations.AlterField(
            model_name='list',
            name='item7',
            field=models.CharField(default='item 7', max_length=600),
        ),
        migrations.AlterField(
            model_name='list',
            name='item8',
            field=models.CharField(default='item 8', max_length=600),
        ),
        migrations.AlterField(
            model_name='list',
            name='item9',
            field=models.CharField(default='item 9', max_length=600),
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(default='Top Ten', max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='horror_type',
            field=models.CharField(choices=[('PSYCHOLOGICAL HORROR', 'Psychological horror'), ('ALIEN', 'Alien'), ('INESCAPABLE', 'Inescapable'), ('PERSONAL HORROR', 'Personal Horror'), ('HORROR MYTH', 'Horror Myth'), ('GHOST HORROR', 'Ghost Horror'), ('ZOMBIE', 'Zombies'), ('HAUNTED HOUSE', 'Haunted House')], default='Horror', max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
