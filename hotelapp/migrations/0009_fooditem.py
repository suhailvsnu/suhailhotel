# Generated by Django 4.2.3 on 2023-09-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0008_rename_menuname_tbl_foodmenu_menuname'),
    ]

    operations = [
        migrations.CreateModel(
            name='fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RestaurantName', models.CharField(max_length=30)),
                ('MenuName', models.CharField(max_length=30)),
                ('MenuItemName', models.CharField(max_length=30)),
                ('Quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('cookingtime', models.CharField(max_length=30)),
                ('status', models.CharField(default='available', max_length=30)),
                ('type', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'fooditem',
            },
        ),
    ]