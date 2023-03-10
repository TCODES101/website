# Generated by Django 4.1.3 on 2022-11-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_alter_rooms_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='bedsitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(default='Bedsitter', max_length=20)),
                ('available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='oneBedroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(default='Bedsitter', max_length=20)),
                ('available', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='rooms',
        ),
    ]
