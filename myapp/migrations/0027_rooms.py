# Generated by Django 4.1.3 on 2022-11-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_money_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(default='', max_length=20)),
                ('available', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
