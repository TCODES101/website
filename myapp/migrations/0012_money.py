# Generated by Django 4.1.3 on 2022-11-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_delete_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]