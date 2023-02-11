from django.db import models
from datetime import datetime
from .utils import get_data


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField()
    current_price = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    old_price = models.PositiveIntegerField(default=0)
    price_diff = models.IntegerField(null=True, blank=True)
    data = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        ordering = ('price_diff', '-created')

    def save(self, *args, **kwargs):
        name, price = get_data(self.url)
        price = int(price[:-1])
        self.name = name
        self.old_price = self.current_price
        if self.old_price != price:
            self.price_diff = round(price - self.old_price, 2)
            self.current_price = price
        else:
            self.price_diff = 0
        return super().save(*args, **kwargs)
