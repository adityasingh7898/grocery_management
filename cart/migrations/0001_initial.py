# Generated by Django 4.2.7 on 2023-12-12 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart_model',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_id', models.PositiveIntegerField()),
                ('item_id', models.PositiveIntegerField()),
            ],
        ),
    ]