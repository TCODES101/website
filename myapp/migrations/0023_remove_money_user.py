# Generated by Django 4.1.3 on 2022-11-26 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_money_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='money',
            name='user',
        ),
    ]