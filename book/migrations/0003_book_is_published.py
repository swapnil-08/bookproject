# Generated by Django 3.2 on 2021-04-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
