# Generated by Django 4.1.3 on 2022-11-27 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_alter_money_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='date',
            field=models.CharField(default='', max_length=20),
        ),
    ]
