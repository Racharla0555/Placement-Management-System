# Generated by Django 4.1.3 on 2022-11-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('annualpack', models.CharField(max_length=50)),
                ('highlights', models.CharField(max_length=100)),
            ],
        ),
    ]
