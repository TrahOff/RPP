from django.contrib.auth.models import User
from django.db import models


class Bonus(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.id_user} {self.amount}'

    class Meta:
        verbose_name = 'Бонусы пользователя'
        verbose_name_plural = 'Бонусы пользователей'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    pName = models.CharField(max_length=1000)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)
    mainImage = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    count = models.IntegerField()
    props = models.TextField()

    def __str__(self):
        return f'{self.pName}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    imageUrl = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.product} {self.imageUrl}'

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'


class Order(models.Model):
    STATUS_CART = '1_cart'
    STATUS_WAITING = '2_waiting'
    STATUS_PAYED = '3_payed'

    STATUS_CHOICE = [
        (STATUS_CART, 'cart'),
        (STATUS_WAITING, 'waiting'),
        (STATUS_PAYED, 'payed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE, default=STATUS_CART)
    full_address = models.CharField(max_length=255, null=True)
    amount = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=None, null=True)
    used_bonuses = models.DecimalField(decimal_places=12, max_digits=20, default=None, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.status}'

    class Meta:
        verbose_name = 'заказ(корзина)'
        verbose_name_plural = 'заказы(корзины)'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.order.id} {self.order} {self.price}'

    class Meta:
        verbose_name = 'содержание заказа'
        verbose_name_plural = 'содержание заказов'


class OrderInfo(models.Model):
    PICKUP = 'самовывоз'
    DELIVERY_BY_COURIER = 'доставка курьером'
    TRANSPORT_COMPANY = 'транспортной компанией'

    METHOD_CHOICE = [
        (PICKUP, 'самовывоз'),
        (DELIVERY_BY_COURIER, 'доставка курьером'),
        (TRANSPORT_COMPANY, 'транспортной компанией'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, default=None, blank=True)
    recipient_first_name = models.CharField(max_length=255)
    recipient_email = models.EmailField()
    recipient_phone_number = models.CharField(max_length=12)
    recipient_address = models.CharField(max_length=255, null=True, default=None, blank=True)
    delivery_method = models.CharField(max_length=255, choices=METHOD_CHOICE, default=PICKUP)
    discount = models.BooleanField(null=True, default=None, blank=True)

    def __str__(self):
        return f'{self.order} {self.recipient_first_name} {self.delivery_method}'

    class Meta:
        verbose_name = 'информация о заказе'
        verbose_name_plural = 'информация о заказах'
