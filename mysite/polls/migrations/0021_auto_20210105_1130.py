# Generated by Django 3.1.2 on 2021-01-05 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_amistad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amistad',
            name='uid1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Alumno1', to='polls.alumno'),
        ),
        migrations.AlterField(
            model_name='amistad',
            name='uid2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Alumno2', to='polls.alumno'),
        ),
    ]