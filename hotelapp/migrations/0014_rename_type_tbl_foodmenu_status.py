# Generated by Django 4.0.4 on 2023-10-25 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0013_tbl_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_foodmenu',
            old_name='type',
            new_name='status',
        ),
    ]
