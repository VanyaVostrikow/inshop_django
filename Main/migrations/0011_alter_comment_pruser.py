# Generated by Django 4.1.7 on 2023-03-07 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0010_remove_comment_prcom_remove_comment_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='PrUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
