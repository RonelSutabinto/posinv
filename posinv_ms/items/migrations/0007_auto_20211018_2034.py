# Generated by Django 3.2.5 on 2021-10-18 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20211018_0929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='id',
            new_name='idunit',
        ),
        migrations.AddField(
            model_name='items',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1993),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
