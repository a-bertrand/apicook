# Generated by Django 2.2.4 on 2019-12-23 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookie', '0004_recipe_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='contributors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop', to=settings.AUTH_USER_MODEL),
        ),
    ]
