# Generated by Django 3.2.9 on 2023-12-22 16:43

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Nombre')),
                ('available', models.BooleanField(blank=True, default=True, verbose_name='Disponible?')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='Cantidad')),
                ('cost', models.BigIntegerField(blank=True, null=True, verbose_name='Costo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
