from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('ByCategory/<int:pk>', views.byCategory, name='category'),
    path('product/<int:pk>', views.show_product, name='product'),
    path('basket/<int:pk>', views.basket, name='basket'),
    path('basket/<int:pk>/new', views.delete_from_basket, name='delete_from_basket'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('order', views.show_order, name='order')
]
