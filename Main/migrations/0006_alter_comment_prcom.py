# Generated by Django 4.1.7 on 2023-03-01 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='PrCom',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.user'),
        ),
    ]