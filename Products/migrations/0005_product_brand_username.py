# Generated by Django 5.1.2 on 2024-11-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_alter_product_highest_bid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand_username',
            field=models.CharField(default='nowhere', max_length=50),
        ),
    ]
