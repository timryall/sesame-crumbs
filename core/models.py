from django.conf import settings
from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    # When the order is first created
    start_date = models.DateTimeField(auto_now_add=True)
    # When the order is offically placed
    ordered_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
