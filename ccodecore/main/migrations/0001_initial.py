# Generated by Django 5.0.6 on 2024-05-21 12:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('nickname', models.CharField(max_length=63)),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(editable=False, max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('creation_data', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]