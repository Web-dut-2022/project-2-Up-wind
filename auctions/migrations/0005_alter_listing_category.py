# Generated by Django 4.0.3 on 2022-04-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('FS', 'Fashion'), ('TY', 'Toys'), ('ET', 'Electronics'), ('HM', 'Home')], max_length=2),
        ),
    ]
