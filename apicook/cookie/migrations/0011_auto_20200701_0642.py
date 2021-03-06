# Generated by Django 2.2.4 on 2020-07-01 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0010_shoplist_shoplistdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='how_many',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='shoppingingredientlist',
            name='bought_status',
            field=models.CharField(choices=[('PARTIAL', 'PARTIAL'), ('COMPLETE', 'COMPLETE'), ('NOTTOUCH', 'NOTTOUCH')], default='NOTTOUCH', max_length=10),
        ),
    ]
