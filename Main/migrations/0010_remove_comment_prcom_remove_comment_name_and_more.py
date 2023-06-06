# Generated by Django 4.1.7 on 2023-03-03 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_alter_order_prname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='PrCom',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='PrProd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='PrUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.user'),
        ),
    ]