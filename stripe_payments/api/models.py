from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Item(models.Model):
    EUR = 'eur'
    USD = 'usd'
    CURRENCY_CHOICES = (
        (EUR, 'eur'),
        (USD, 'usd')
    )

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
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='eur',
        verbose_name='Валюта'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)


class Coupon(models.Model):
    ONCE = 'O'
    REPEATED = 'R'
    FOREVER = 'F'
    DURATION_CHOICES = (
        (ONCE, 'once'),
        (REPEATED, 'repeated'),
        (FOREVER, 'forever'),
    )

    amount_off = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Размер скидки'
    )
    currency = models.CharField(
        max_length=3,
        default='eur',
        verbose_name='Валюта'
    )
    duration = models.CharField(
        max_length=1,
        choices=DURATION_CHOICES,
        default=ONCE
    )
    duration_in_months = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Срок действия скидки'
    )
    percent_off = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Процент скидки'
    )

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'


class Order(models.Model):
    OPEN = 'OPN'
    SUBMITTED = 'SBM'
    PROCESSING = 'PRS'
    COMPLETE = "CMP"
    CANCELED = 'CNL'

    STATUS_CHOICES = (
        (OPEN, 'open'),
        (SUBMITTED, 'submitted'),
        (PROCESSING, 'processing'),
        (COMPLETE, 'complete'),
        (CANCELED, 'canceled'),
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Покупатель'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name='Дата создания'
    )
    date_completed = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата исполнения'
    )
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=OPEN,
        verbose_name='Статус заказа',
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_total_price(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total_item_price()
        return total

    def __str__(self):
        return f'{self.customer.username} - {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='orderitems',
        verbose_name='Заказ'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='items_list',
        verbose_name='Товары'
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Позиции в заказе'
        verbose_name_plural = 'Позиции в заказе'

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"


class Discount(models.Model):
    coupon = models.ForeignKey(
        Coupon,
        on_delete=models.CASCADE,
        verbose_name='Купон'
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Покупатель'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='discounts',
        verbose_name='Скидки'
    )
    date_end = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Срок окончания действия'
    )
    date_applied = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата использования купона'
    )

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
