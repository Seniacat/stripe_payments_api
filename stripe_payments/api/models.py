from http.client import PROCESSING
from tkinter.messagebox import CANCEL
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Item(models.Model):
    
    name = models.CharField(
        max_length=256,
        verbose_name='Название продукта' 
    )
    description = models.TextField(
        verbose_name='Описание продукта'
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name='Цена'
    )
    # currency = 

    def __str__(self) -> str:
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)


class Discount(models.Model):
    # coupon_id =  
    pass


class Order(models.Model):
    OPEN = 'OPN',
    SUBMITTED = 'SBM'
    PROCESSING = 'PRS'
    COMPLETE = "CMP"
    CANCELED = 'CNL'

    CHOICES = (
        (OPEN, 'open'),
        (SUBMITTED, 'submitted'),
        (PROCESSING, 'processing'),
        (COMPLETE, 'complete'),
        (CANCELED, 'canceled'),
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        verbose_name='Покупатель')
    orderitems = models.ManyToManyField(
        Item,
        through='ItemsInOrder',
        through_fields=('item', 'order'),
        verbose_name='Товары в заказе'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        null = True,
        blank = True,
        verbose_name='Дата создания'    
    )
    date_completed = models.DateTimeField(
        null = True,
        blank = True,
        verbose_name='Дата исполнения'
    )
    status = models.CharField(
        'Статус заказа',
        max_length=3,
        choices=CHOICES,
        default=OPEN
    )
    discounts = models.ManyToManyField(
        Discount,
        verbose_name='Скидки'
    )
    amount_total = models.PositiveIntegerField(
        default=0,
        verbose_name='Сумма'
    )
    

class ItemsInOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items_in_order',
        verbose_name='Заказ'
    )
    items = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='items_list',
        verbose_name='Товары'
    )
    quantity = models.PositiveSmallIntegerField('Количество')