# Generated by Django 3.2.9 on 2021-12-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0009_booking_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_guests',
            field=models.IntegerField(default=0),
        ),
    ]
