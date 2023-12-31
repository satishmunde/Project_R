# Generated by Django 4.1.7 on 2023-08-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                    "p_img",
                    models.FileField(
                        default=None, max_length=250, null=True, upload_to="Items/"
                    ),
                ),
                ("p_title", models.CharField(max_length=100)),
                ("p_desc", models.TextField()),
                ("p_price", models.BigIntegerField()),
                ("p_id", models.BigIntegerField()),
            ],
        ),
    ]
