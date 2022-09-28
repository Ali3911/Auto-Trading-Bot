# Generated by Django 4.0.3 on 2022-03-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BinanceSymbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tokenA', models.CharField(max_length=200)),
                ('tokenB', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BinanceTimeFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_period', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_symbol', models.CharField(max_length=100)),
                ('order_side', models.CharField(max_length=50)),
                ('order_price', models.FloatField()),
                ('order_qty', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfitRatio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit_loss', models.FloatField()),
            ],
        ),
    ]
