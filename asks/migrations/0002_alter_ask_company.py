# Generated by Django 5.1.6 on 2025-03-05 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("asks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ask",
            name="company",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="소속"
            ),
        ),
    ]
