# Generated by Django 3.2.9 on 2023-12-22 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='cost',
            new_name='value',
        ),
    ]
