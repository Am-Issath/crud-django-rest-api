# Generated by Django 5.0.2 on 2024-02-09 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publish_date',
            new_name='publication_date',
        ),
    ]
