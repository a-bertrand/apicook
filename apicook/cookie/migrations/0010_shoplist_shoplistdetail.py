# Generated by Django 2.2.4 on 2020-06-25 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookie', '0009_auto_20200216_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contributors', models.ManyToManyField(blank=True, related_name='shop_list', to=settings.AUTH_USER_MODEL)),
                ('recipes', models.ManyToManyField(blank=True, to='cookie.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='ShopListDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_value', models.IntegerField(default=0)),
                ('bought_status', models.CharField(choices=[('PARTIAL', 'PARTIAL'), ('COMPLETE', 'COMPLETE'), ('NOTTOUCH', 'COMPLETE')], default='NOTTOUCH', max_length=10)),
                ('measure_type', models.CharField(choices=[('x', 'x'), ('kilogramme', 'kilogramme'), ('gramme', 'gramme'), ('litre', 'litre'), ('centilitre', 'centilitre'), ('millilitre', 'millilitre')], max_length=20, verbose_name='Type de mesure')),
                ('total_quantity', models.IntegerField(blank=True, null=True, verbose_name='Quantité')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_list_detail', to='cookie.Article')),
                ('shop_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_content', to='cookie.ShopList')),
            ],
        ),
    ]
