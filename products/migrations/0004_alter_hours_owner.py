# Generated by Django 3.2.5 on 2024-01-07 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20240107_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours',
            name='owner',
            field=models.ForeignKey(default=45, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
