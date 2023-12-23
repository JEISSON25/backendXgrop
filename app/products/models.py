from model_utils.models import TimeStampedModel
from django.db import models


class Products(TimeStampedModel):
    name = models.CharField(
        'Nombre', unique=True,  max_length=50, blank=True, null=True)
    available = models.BooleanField(
        'Disponible?', default=True, blank=True)
    amount = models.IntegerField(
        'Cantidad',  blank=True, null=True)
    value = models.BigIntegerField(
        'Costo',  blank=True, null=True)

    def __str__(self):

        return f'{self.name}  - {self.available} - {self.amount} - {self.value} '
