# Generated by Django 4.1.3 on 2022-12-03 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_alter_reservation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='timeslot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.timeslot'),
        ),
    ]
