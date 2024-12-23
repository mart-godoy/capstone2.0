# Generated by Django 5.1.3 on 2024-11-07 19:32

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("nombre", models.CharField(max_length=50)),
            ],
            options={"verbose_name_plural": "Categorías",},
        ),
        migrations.CreateModel(
            name="Marca",
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
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
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
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
                (
                    "precio",
                    models.PositiveIntegerField(
                        help_text="Precio en pesos chilenos (CLP)",
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                ("stock", models.PositiveIntegerField(default=0)),
                ("imagen", models.ImageField(upload_to="productos/")),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                (
                    "sku",
                    models.CharField(blank=True, max_length=50, null=True, unique=True),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lukaspet_app.categoria",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lukaspet_app.marca",
                    ),
                ),
            ],
        ),
    ]
