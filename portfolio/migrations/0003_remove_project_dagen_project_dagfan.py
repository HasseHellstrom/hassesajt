# Generated by Django 4.0 on 2021-12-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_dagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='dagen',
        ),
        migrations.AddField(
            model_name='project',
            name='dagfan',
            field=models.DateField(default='date.today'),
        ),
    ]
