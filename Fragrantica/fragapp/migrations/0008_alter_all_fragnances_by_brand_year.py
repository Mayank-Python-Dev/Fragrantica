# Generated by Django 3.2.8 on 2021-10-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fragapp', '0007_auto_20211018_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_fragnances_by_brand',
            name='year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]