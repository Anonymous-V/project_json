# Generated by Django 3.0.4 on 2020-03-07 15:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200307_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusers',
            name='api_key',
            field=models.UUIDField(default=uuid.UUID('e6e82f0c-1167-4467-9778-9e170e4c9300'), primary_key=True, serialize=False),
        ),
    ]