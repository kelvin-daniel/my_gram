# Generated by Django 3.1.2 on 2020-10-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_gram', '0003_auto_20201011_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]