# Generated by Django 4.1.3 on 2022-12-04 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manageresorder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='customerName',
        ),
        migrations.AlterField(
            model_name='customer',
            name='reservationC',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manageresorder.reservation'),
        ),
    ]