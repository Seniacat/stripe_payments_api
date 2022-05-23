from django.db import models


class Item(models.Model):
    
    name = models.CharField(
        max_length=256,
        verbose_name='Название продукта' 
    )
    description = models.TextField(
        verbose_name='Описание продукта'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )

    def __str__(self) -> str:
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
