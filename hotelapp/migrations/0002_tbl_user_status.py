# Generated by Django 4.2.3 on 2023-09-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_user',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
