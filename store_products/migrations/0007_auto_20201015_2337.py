# Generated by Django 3.1.2 on 2020-10-15 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_products', '0006_auto_20201015_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_has_size',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]