# Generated by Django 4.2.13 on 2024-06-10 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leilao', '0009_realestate_increment_value_realestate_starting_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='bid_history',
            field=models.JSONField(default=list),
        ),
    ]
