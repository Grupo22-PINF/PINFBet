# Generated by Django 3.1.2 on 2020-12-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20201221_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumasig',
            name='nminima',
            field=models.IntegerField(default=0),
        ),
    ]