from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from orders.utils import format_number
from orders.models import Order, OrderItem
from carts.models import Cart
from orders.forms import CreateOrderForm


class CreateOrderView(LoginRequiredMixin, FormView):
    template_name = "orders/create_order.html"
    form_class = CreateOrderForm
    success_url = reverse_lazy('users:profile')

    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        return initial
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form_data = self.request.session.get("order_form_data", None)
        if form_data:
            for key, value in form_data.items():
                print(key, value)
                if key == 'phone_number':
                    form.fields[key].initial = format_number(value)
                else:
                    form.fields[key].initial = value 
        return form

    def form_valid(self, form):
        try:
            with transaction.atomic():
                user = self.request.user
                cart_items = Cart.objects.filter(user=user)

                if cart_items.exists():
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data["phone_number"],
                        requires_delivery=form.cleaned_data["requires_delivery"],
                        delivery_address=form.cleaned_data["delivery_address"],
                        payment_on_get=form.cleaned_data["payment_on_get"],
                    )
                    for cart_item in cart_items:
                        product = cart_item.product
                        name = cart_item.product.name
                        price = cart_item.product.sell_price()
                        quantity = cart_item.quantity

                        if product.quantity < quantity:
                            raise ValidationError(
                                f"Недостаточно количество товара {name} на складе\
                                                В наличи - {product.quantity}"
                            )

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )

                        product.quantity -= quantity
                        product.save()

                cart_items.delete()

                messages.success(self.request, "Заказ оформлен!")
                return redirect("user:profile")
        except ValidationError as e:
            self.request.session["order_form_data"] = form.cleaned_data
            messages.warning(self.request, str(*e))
            return redirect("orders:create_order")
        
    def form_invalid(self, form):
        if 'delivery_address' in form.errors:
            messages.warning(self.request, form.errors['delivery_address'])
        else: 
            messages.warning(self.request, 'Заполните все обязательные поля!')
        self.request.session["order_form_data"] = form.cleaned_data
        return redirect('orders:create_order')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "TechKing - `Оформление заказа"
        context['order'] = True
        return context
