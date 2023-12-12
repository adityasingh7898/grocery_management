# Generated by Django 4.2.7 on 2023-12-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buy_model',
            fields=[
                ('buy_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('t_price', models.PositiveIntegerField()),
            ],
        ),
    ]
