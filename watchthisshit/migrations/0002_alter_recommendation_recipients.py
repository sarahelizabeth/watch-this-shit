# Generated by Django 3.2.19 on 2023-06-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchthisshit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='recipients',
            field=models.ManyToManyField(blank=True, related_name='received_recs', to='watchthisshit.Profile'),
        ),
    ]
