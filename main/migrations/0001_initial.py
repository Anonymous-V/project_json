# Generated by Django 3.0.4 on 2020-03-07 14:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('email', models.EmailField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('api_key', models.UUIDField(default=uuid.UUID('294bd34e-63c5-41d3-b3eb-697c771a2351'), primary_key=True, serialize=False)),
            ],
        ),
    ]
