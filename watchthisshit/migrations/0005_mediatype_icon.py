# Generated by Django 3.2.19 on 2023-06-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchthisshit', '0004_auto_20230615_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediatype',
            name='icon',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
