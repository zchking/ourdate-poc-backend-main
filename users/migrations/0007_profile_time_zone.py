# Generated by Django 4.1.5 on 2023-02-10 07:55

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_alcohol_usage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='time_zone',
            field=timezone_field.fields.TimeZoneField(default='America/Los_Angeles'),
        ),
    ]
