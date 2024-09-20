# Generated by Django 5.1.1 on 2024-09-20 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("subtitle", models.CharField(max_length=250)),
                ("author", models.CharField(max_length=100)),
                ("ISBN", models.CharField(max_length=13)),
            ],
        ),
    ]
