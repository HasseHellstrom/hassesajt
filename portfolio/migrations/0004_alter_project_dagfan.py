# Generated by Django 4.0 on 2021-12-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_project_dagen_project_dagfan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='dagfan',
            field=models.DateField(default='1/1/1900'),
        ),
    ]
