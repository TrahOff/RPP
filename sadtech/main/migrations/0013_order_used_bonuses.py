# Generated by Django 4.2.1 on 2023-06-02 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='used_bonuses',
            field=models.DecimalField(decimal_places=12, default=None, max_digits=20, null=True),
        ),
    ]