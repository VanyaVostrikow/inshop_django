# Generated by Django 4.1.7 on 2023-03-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_alter_order_prname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='logo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
