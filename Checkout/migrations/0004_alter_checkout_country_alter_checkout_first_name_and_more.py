# Generated by Django 5.0.6 on 2024-11-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checkout', '0003_checkout_country_checkout_email_checkout_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='country',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
