# Generated by Django 4.2.6 on 2023-10-15 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='url',
            new_name='slug',
        ),
    ]
