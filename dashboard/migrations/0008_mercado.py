# Generated by Django 4.2.2 on 2023-06-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0007_alter_empresa_usuarios"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mercado",
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
                ("mercado", models.CharField(max_length=200)),
            ],
        ),
    ]
