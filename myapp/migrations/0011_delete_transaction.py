# Generated by Django 4.1.3 on 2022-11-25 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_transaction_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='transaction',
        ),
    ]
