# Generated by Django 5.1.2 on 2024-12-02 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_bid_bid_time_product_startdt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ['-bid_time']},
        ),
    ]
