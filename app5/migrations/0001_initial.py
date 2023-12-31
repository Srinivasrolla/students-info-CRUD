# Generated by Django 4.2.5 on 2023-10-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('course', models.CharField(max_length=40)),
                ('fee', models.BigIntegerField()),
                ('assignment1', models.BigIntegerField()),
                ('assignment2', models.BigIntegerField()),
                ('assignment3', models.BigIntegerField()),
                ('assignment4', models.BigIntegerField()),
                ('institute', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
            ],
        ),
    ]
