from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    class Status(models.TextChoices):
        waiting_status = 'WS', _('Waiting_status')
        decline_status = 'DS', _('Decline_status')
        accepted_status = 'AS', _('Accepted_status')

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.waiting_status,
    )

    customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE)
    courier = models.ForeignKey('users.Courier', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=100000, decimal_places=2)


class OrderProduct(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()



