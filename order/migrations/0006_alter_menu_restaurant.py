# Generated by Django 4.1.3 on 2022-12-03 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_menu_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.restaurant', unique=True),
        ),
    ]