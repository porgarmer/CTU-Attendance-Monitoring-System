# Generated by Django 3.2.3 on 2021-05-26 09:05

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('properties', jsonfield.fields.JSONField(null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('key_type', models.CharField(default='TOTP', max_length=25)),
                ('enabled', models.BooleanField(default=True)),
                ('expires', models.DateTimeField(blank=True, default=None, null=True)),
                ('last_used', models.DateTimeField(blank=True, default=None, null=True)),
                ('owned_by_enterprise', models.BooleanField(blank=True, default=None, null=True)),
            ],
        ),
    ]