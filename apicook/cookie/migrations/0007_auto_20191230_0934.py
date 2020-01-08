# Generated by Django 2.2.4 on 2019-12-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0006_auto_20191223_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='shoplist',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='shoplist',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='shop',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
