# Generated by Django 5.0.1 on 2024-01-11 01:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RSVP",
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
                ("attending", models.BooleanField()),
                ("not_attending", models.BooleanField()),
                ("name", models.TextField(max_length=500)),
                ("dietary_restrictions", models.TextField(blank=True)),
                ("observations", models.TextField(blank=True)),
            ],
        ),
    ]
