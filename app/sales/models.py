from model_utils.models import TimeStampedModel
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from ..products.models import Products


class Sales(TimeStampedModel):
    date = models.DateField(
        'Fecha de factura',  blank=True, null=True)

    value = models.BigIntegerField(
        'Valor total', default=True, blank=True, null=True)

    amount = models.IntegerField(
        'Cantidad',  blank=True, null=True)

    products = models.ForeignKey(
        Products,
        verbose_name="Products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):

        return f'{self.date}  - {self.products} - {self.value} '


@receiver(post_save, sender=Sales)
def set_amount(sender, instance, created, **kwargs):

    if created:
        amount = instance.products.amount - instance.amount
        instance.products.amount = amount
        instance.products.save()
