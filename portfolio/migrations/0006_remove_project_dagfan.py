# Generated by Django 4.0 on 2021-12-28 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_project_dagfan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='dagfan',
        ),
    ]
