# Generated by Django 5.1.4 on 2025-01-02 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_suff',
            new_name='user_suffix',
        ),
    ]