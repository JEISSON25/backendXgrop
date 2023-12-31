# Generated by Django 3.2.9 on 2023-12-22 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_cost_products_value'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='sales',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.products', verbose_name='Products'),
        ),
        migrations.DeleteModel(
            name='DetailSales',
        ),
    ]
