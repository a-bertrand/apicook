# Generated by Django 2.2.4 on 2019-12-09 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0002_auto_20191209_1143'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Steps',
            new_name='Step',
        ),
        migrations.RenameField(
            model_name='step',
            old_name='recipes',
            new_name='recipe',
        ),
    ]