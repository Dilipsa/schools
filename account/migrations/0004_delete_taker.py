# Generated by Django 3.1.7 on 2021-05-02 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_taker'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Taker',
        ),
    ]
