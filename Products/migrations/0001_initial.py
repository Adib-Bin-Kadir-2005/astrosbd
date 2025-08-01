# Generated by Django 5.1.2 on 2024-11-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('brand_name', models.CharField(max_length=255)),
                ('starting_price', models.FloatField()),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
