from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_backends, login as auth_login
from carts.models import Cart

def redirect_to_login_view(strategy, backend, user, request=None, *args, **kwargs):
    if user and request:

        session_key = request.session.session_key
        
        user.backend = backend if isinstance(backend, str) else get_backends()[0].__module__ + "." + get_backends()[0].__class__.__name__
        auth_login(request, user)

        if session_key:
            forgot_carts = Cart.objects.filter(user=user)
            if forgot_carts.exists():
                    forgot_carts.delete()
            Cart.objects.filter(session_key=session_key).update(user=user)
        
        messages.success(request, f"{user.username}, Вы вошли в аккаунт")

        next_url = request.session.get('next', reverse('main:index'))
        if next_url != reverse('user:logout'):
            return redirect(next_url)
        else:
            return reverse_lazy('main:index')
