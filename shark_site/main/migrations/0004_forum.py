# Generated by Django 4.2.7 on 2023-11-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Forum",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
