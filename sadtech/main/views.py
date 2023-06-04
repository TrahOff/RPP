import datetime

from django.contrib.auth import login, logout
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models import Q

from .forms import *
from .models import *


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    cart = None
    print(request.user)
    if request.user:
        if not AnonymousUser.is_anonymous:
            cart = Order.objects.filter(
                user=request.user, status=Order.STATUS_CART
            ).first()
            if not cart:
                cart = Order.objects.create(
                    user=request.user, status=Order.STATUS_CART, amount=0
                )

    orderItems = OrderItems.objects.filter(order=cart)

    fullPrice = 0
    for elem in orderItems:
        fullPrice += elem.price

    count = ''

    if cart:
        if cart.amount == 0:
            count = 'пуста'
        if cart.amount % 10 == 1:
            count = f'{cart.amount} товар'
        if 1 < cart.amount % 10 < 5:
            count = f'{cart.amount} товара'
        if cart.amount % 10 >= 5:
            count = f'{cart.amount} товаров'

    data = {
        'prod': products,
        'cat': categories,
        'cart': cart,
        'count': count
    }
    return render(request, 'main/main.html', data)


def byCategory(request, pk):
    cat = Category.objects.get(id=pk)
    products = Product.objects.filter(cat=cat)
    categories = Category.objects.all()
    cart = None
    if not AnonymousUser.is_anonymous:
        cart = Order.objects.filter(
            user=request.user, status=Order.STATUS_CART
        ).first()
        if not cart:
            cart = Order.objects.create(
                user=request.user, status=Order.STATUS_CART, amount=0
            )

    orderItems = OrderItems.objects.filter(order=cart)

    fullPrice = 0
    for elem in orderItems:
        fullPrice += elem.price

    count = ''

    if cart:
        if cart.amount == 0:
            count = 'пуста'
        if cart.amount % 10 == 1:
            count = f'{cart.amount} товар'
        if 1 < cart.amount % 10 < 5:
            count = f'{cart.amount} товара'
        if cart.amount % 10 >= 5:
            count = f'{cart.amount} товаров'

    data = {
        'prod': products,
        'cat': categories,
        'cart': cart,
        'count': count
    }

    return render(request, 'main/main.html', data)


def show_product(request, pk):
    prod = Product.objects.get(pk=pk)
    imgs = Images.objects.filter(product=prod)
    print(prod)
    print(imgs)
    mainImg = imgs[0]
    cart = None
    if not AnonymousUser.is_anonymous:
        cart = Order.objects.filter(
            user=request.user, status=Order.STATUS_CART
        ).first()
        if not cart:
            cart = Order.objects.create(
                user=request.user, status=Order.STATUS_CART, amount=0
            )

    orderItems = OrderItems.objects.filter(order=cart)

    fullPrice = 0
    for elem in orderItems:
        fullPrice += elem.price

    count = ''

    if cart:
        if cart.amount == 0:
            count = 'пуста'
        if cart.amount % 10 == 1:
            count = f'{cart.amount} товар'
        if 1 < cart.amount % 10 < 5:
            count = f'{cart.amount} товара'
        if cart.amount % 10 >= 5:
            count = f'{cart.amount} товаров'

    data = {
        'Product': prod,
        'imgs': imgs,
        'mainImg': mainImg,
        'cart': cart,
        'count': count
    }

    return render(request, 'main/product.html', data)


def basket(request, pk):
    if request.user.is_authenticated:
        if Product.objects.filter(pk=pk):
            prod = Product.objects.get(pk=pk)
            cart = Order.objects.filter(
                user=request.user, status=Order.STATUS_CART
            ).first()
            if not cart:
                cart = Order.objects.create(
                    user=request.user, status=Order.STATUS_CART, amount=0
                )

            orderItem = OrderItems.objects.filter(order=cart, product=prod)
            if not orderItem:
                OrderItems.objects.create(
                    order=cart, product=prod, price=prod.price
                )
                amount = cart.amount + 1
                cart.amount = amount
                cart.save()

            if request.method == 'POST':
                orderItems = request.POST.getlist('orderItems')
                for item in orderItems:
                    OrderItems.objects.get(pk=item).delete()
                    cart.amount -= 1
                    cart.save()

            orderItems = OrderItems.objects.filter(order=cart)

            fullPrice = 0
            for elem in orderItems:
                fullPrice += elem.price

            count = ''

            if cart.amount == 0:
                count = 'пуста'
            if cart.amount % 10 == 1:
                count = f'{cart.amount} товар'
            if 1 < cart.amount % 10 < 5:
                count = f'{cart.amount} товара'
            if cart.amount % 10 >= 5:
                count = f'{cart.amount} товаров'

            data = {
                'orderItems': orderItems,
                'fullPrice': fullPrice,
                'cart': cart,
                'count': count
            }
        else:
            cart = Order.objects.filter(
                user=request.user, status=Order.STATUS_CART
            ).first()

            if not cart:
                cart = Order.objects.create(
                    user=request.user, status=Order.STATUS_CART, amount=0
                )

            if request.method == 'POST':
                orderItems = request.POST.getlist('orderItems')
                for item in orderItems:
                    OrderItems.objects.get(pk=item).delete()
                    cart.amount -= 1
                    cart.save()

            orderItems = OrderItems.objects.filter(order=cart)

            fullPrice = 0
            for elem in orderItems:
                fullPrice += elem.price

            count = ''

            if cart.amount == 0:
                count = 'пуста'
            if cart.amount % 10 == 1:
                count = f'{cart.amount} товар'
            if 1 < cart.amount % 10 < 5:
                count = f'{cart.amount} товара'
            if cart.amount % 10 >= 5:
                count = f'{cart.amount} товаров'

            data = {
                'orderItems': orderItems,
                'fullPrice': fullPrice,
                'cart': cart,
                'count': count
            }

        return render(request, 'main/basket.html', data)
    else:
        return render(request, 'main/register.html')


def delete_from_basket(request, pk):
    OrderItems.objects.get(pk=pk).delete()
    cart = None

    if request.user:
        cart = Order.objects.filter(
            user=request.user, status=Order.STATUS_CART
        ).first()

        amount = cart.amount - 1
        cart.amount = amount
        cart.save()

    orderItems = OrderItems.objects.filter(order=cart)

    fullPrice = 0
    for elem in orderItems:
        fullPrice += elem.price

    count = ''

    if cart.amount == 0:
        count = 'пуста'
    if cart.amount % 10 == 1:
        count = f'{cart.amount} товар'
    if 1 < cart.amount % 10 < 5:
        count = f'{cart.amount} товара'
    if cart.amount % 10 >= 5:
        count = f'{cart.amount} товаров'

    data = {
        'orderItems': orderItems,
        'fullPrice': fullPrice,
        'cart': cart,
        'count': count
    }

    return render(request, 'main/basket.html', data)


def delete_by_checkbox(request):
    if request.method == 'POST':
        orderItems = request.POST.getlist('orderItems')
        print(orderItems)

    cart = Order.objects.filter(
        user=request.user, status=Order.STATUS_CART
    ).first()

    orderItems = OrderItems.objects.filter(order=cart)

    fullPrice = 0
    for elem in orderItems:
        fullPrice += elem.price

    count = ''

    if cart.amount == 0:
        count = 'пуста'
    if cart.amount % 10 == 1:
        count = f'{cart.amount} товар'
    if 1 < cart.amount % 10 < 5:
        count = f'{cart.amount} товара'
    if cart.amount % 10 >= 5:
        count = f'{cart.amount} товаров'

    data = {
        'orderItems': orderItems,
        'fullPrice': fullPrice,
        'cart': cart,
        'count': count
    }

    return render(request, 'main/basket.html', data)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        initial_bonus(self.request.user.id)
        return redirect('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('main')


def initial_bonus(pk):
    bonus = Bonus.objects.create(id_user_id=pk, amount=1000)
    return bonus


def profile(request):
    user_bonus = Bonus.objects.get(id_user=request.user)
    cart = Order.objects.filter(
        user=request.user, status=Order.STATUS_CART
    ).first()
    if not cart:
        cart = Order.objects.create(
            user=request.user, status=Order.STATUS_CART, amount=0
        )

    orderItems = OrderItems.objects.filter(order=cart)
    userOrders = Order.objects.filter(Q(user=request.user) & ~Q(status=Order.STATUS_CART))
    fullPrice = 0
    for elem in orderItems:
        fullPrice += elem.price

    count = ''

    if cart.amount == 0:
        count = 'пуста'
    if cart.amount % 10 == 1:
        count = f'{cart.amount} товар'
    if 1 < cart.amount % 10 < 5:
        count = f'{cart.amount} товара'
    if cart.amount % 10 >= 5 or 10 <= cart.amount % 100 >= 5 < 21:
        count = f'{cart.amount} товаров'

    data = {
        'bonus': user_bonus.amount,
        'cart': cart,
        'count': count,
        'UserOrders': userOrders
    }

    return render(request, 'main/profile.html', data)


def show_order(request):
    error = ''
    cart = Order.objects.filter(
        user=request.user, status=Order.STATUS_CART
    ).first()
    form = RegisterOrderForm(initial={'order': cart, 'recipient_address': None})
    orderItems = OrderItems.objects.filter(order=cart)
    user_bonus = Bonus.objects.get(id_user=request.user)
    choices = {
        'self': 'самовывоз',
        'courier': 'доставка курьером',
        'tc': 'транспортной компанией',
    }

    choice = choices['self']

    fullPrice = 0
    for elem in orderItems:
        fullPrice += elem.price

    count = ''

    if cart.amount == 0:
        count = 'пуста'
    if cart.amount % 10 == 1:
        count = f'{cart.amount} товар'
    if 1 < cart.amount % 10 < 5:
        count = f'{cart.amount} товара'
    if cart.amount % 10 >= 5:
        count = f'{cart.amount} товаров'

    if request.method == 'POST':
        form = RegisterOrderForm(request.POST, initial={'order': cart, 'recipient_address': None})
        if form.is_valid():
            print('yes')
            form.save()
            tmp = OrderInfo.objects.all().last()

            cart.status = Order.STATUS_WAITING
            cart.price = fullPrice
            cart.used_bonuses = 0

            if tmp.discount:
                cart.price = cart.price - user_bonus.amount
                cart.used_bonuses = user_bonus.amount
                user_bonus.amount = 0
                user_bonus.save()

            cart.save()
            return redirect('profile')
        else:
            print(form['recipient_email'])
            error = 'пустые поля'

    data = {
        'error': error,
        'cart': cart,
        'form': form,
        'fullPrice': fullPrice,
        'count': count,
        'choice': choice,
        'getDate': datetime.date.today() + datetime.timedelta(days=5),
        'userBonus': user_bonus
    }

    return render(request, 'main/order.html', data)
