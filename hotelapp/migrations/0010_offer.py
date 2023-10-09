# Generated by Django 4.2.3 on 2023-10-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0009_fooditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Res_id', models.CharField(max_length=30)),
                ('MenuItemName', models.CharField(max_length=30)),
                ('offer', models.CharField(max_length=30)),
                ('startdate', models.CharField(max_length=30)),
                ('enddate', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'offer',
            },
        ),
    ]
