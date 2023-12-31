# Generated by Django 4.2.1 on 2023-07-12 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('dob', models.DateField()),
                ('doa', models.DateField()),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=70)),
                ('item_price', models.FloatField()),
                ('item_qty', models.IntegerField(max_length=5)),
                ('vendor_name', models.CharField(max_length=100)),
                ('dop', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SBT.user')),
            ],
        ),
    ]
