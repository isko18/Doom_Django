# Generated by Django 4.2.3 on 2023-07-08 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_socialnetworks_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialnetworks',
            old_name='google',
            new_name='email',
        ),
    ]
