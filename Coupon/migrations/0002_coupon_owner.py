# Generated by Django 4.1.7 on 2023-03-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coupon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='owner',
            field=models.CharField(max_length=129, null=True),
        ),
    ]
