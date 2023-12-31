# Generated by Django 4.1.7 on 2023-08-05 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserDtl",
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
                (
                    "fname",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="First_Name"
                    ),
                ),
                (
                    "lname",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Last_Name"
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phoneNo", models.IntegerField(verbose_name="Phone Number")),
                ("addressLine1", models.TextField(verbose_name="Address Line 1")),
                ("addressLine2", models.TextField(verbose_name="Address Line 2")),
                ("state", models.CharField(max_length=20, verbose_name="State")),
                ("country", models.CharField(max_length=20)),
                ("zipCode", models.PositiveSmallIntegerField()),
            ],
        ),
    ]
