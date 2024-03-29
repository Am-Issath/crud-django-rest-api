# Generated by Django 5.0.2 on 2024-02-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ISBN', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publish_date', models.DateField()),
            ],
            options={
                'db_table': 'books_db',
            },
        ),
    ]
