# Generated by Django 4.1 on 2022-08-13 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("brand", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
                ("year", models.IntegerField()),
                ("hp", models.IntegerField()),
                ("color", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
                ("type", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Client",
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
                ("mail", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("first_name", models.CharField(max_length=100)),
                ("second_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Receipt",
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
                    "car_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="myapp.car"
                    ),
                ),
                (
                    "client_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="myapp.client",
                    ),
                ),
            ],
        ),
    ]