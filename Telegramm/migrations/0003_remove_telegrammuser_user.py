# Generated by Django 4.1.7 on 2023-03-27 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Telegramm', '0002_alter_telegrammuser_chat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegrammuser',
            name='user',
        ),
    ]
