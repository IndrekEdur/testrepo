# Generated by Django 3.2.5 on 2024-01-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_project_project_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_number',
            field=models.IntegerField(unique=True),
        ),
    ]