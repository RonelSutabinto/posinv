# Generated by Django 3.2.5 on 2021-09-23 04:22

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('itemcode', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=85)),
                ('brand', models.CharField(max_length=45)),
                ('category', models.CharField(max_length=45)),
                ('unit', models.CharField(max_length=45)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('saleprice', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('pricingbyID', models.CharField(max_length=45)),
                ('pricingdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='itemserials',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('itemcode', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=85)),
                ('brand', models.CharField(max_length=45)),
                ('category', models.CharField(max_length=45)),
                ('unit', models.CharField(max_length=45)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('saleprice', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('pricingbyID', models.CharField(max_length=45)),
                ('pricingdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'itemserials',
            },
        ),
        migrations.CreateModel(
            name='itemserials_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('itemcode', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=85)),
                ('brand', models.CharField(max_length=45)),
                ('category', models.CharField(max_length=45)),
                ('unit', models.CharField(max_length=45)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('saleprice', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('pricingbyID', models.CharField(max_length=45)),
                ('pricingdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'itemserials_details',
            },
        ),
    ]
