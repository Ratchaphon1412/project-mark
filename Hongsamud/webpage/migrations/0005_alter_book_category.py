# Generated by Django 4.1.4 on 2023-04-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webpage", "0004_rename_type_book_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="category",
            field=models.CharField(
                choices=[
                    ("01", "Novels"),
                    ("02", "Kids"),
                    ("03", "Academic"),
                    ("04", "Magazine"),
                    ("05", "Doujin"),
                    ("06", "Cartoon"),
                    ("07", "Religion"),
                ],
                max_length=20,
            ),
        ),
    ]
