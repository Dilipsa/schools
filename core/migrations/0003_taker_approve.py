# Generated by Django 3.1.7 on 2021-05-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210502_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='taker',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
