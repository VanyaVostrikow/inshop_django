# Generated by Django 4.1.7 on 2023-03-01 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_comment_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
