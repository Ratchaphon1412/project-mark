# Generated by Django 4.1.2 on 2023-04-03 05:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webpage", "0002_book_description_alter_book_genre_alter_book_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="image_link",
            field=models.TextField(null=True),
        ),
    ]
