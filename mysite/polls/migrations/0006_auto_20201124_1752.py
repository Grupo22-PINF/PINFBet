# Generated by Django 3.1.2 on 2020-11-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20201124_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='name',
            field=models.CharField(default='ELISEO', max_length=20),
        ),
        migrations.AddField(
            model_name='alumno',
            name='surname',
            field=models.CharField(default='FDEZ', max_length=30),
        ),
    ]