# Generated by Django 3.0.2 on 2020-01-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kart', '0003_auto_20200123_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_delivery_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_shopping_user',
            field=models.BooleanField(default=False),
        ),
    ]