# Generated by Django 4.1.3 on 2022-12-03 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_remove_fnbchoice_fnb_fnbchoice_fnb'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.restaurant'),
        ),
    ]