# Generated by Django 4.1.7 on 2023-03-10 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='add_datetime',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='quantity',
            new_name='num',
        ),
    ]
