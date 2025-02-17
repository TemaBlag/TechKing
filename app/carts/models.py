from statistics import quantiles
from tabnanny import verbose
from xml.sax.handler import property_interning_dict
from django.contrib import sessions
from django.db import models

from users.models import User
from goods.models import Products

class CartQueryset(models.QuerySet):
   
   def total_price(self):
       return sum(cart.products_price() for cart in self)
   
   def total_quantity(self):
       if self:
           return sum(cart.quantity for cart in self)
       return 0

class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table= 'cart'
        verbose_name = "Корзину"
        verbose_name_plural = "Корзина"
        ordering = ("id", )

    objects = CartQueryset().as_manager()

    def __str__(self):
        if self.user:
            return f"Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"
        
        return f"Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}"
    
    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
