from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name= 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Techking - Главная'
        context["content"] = 'Магазин техники Techking'
        return context


class ContactInformationView(TemplateView):
    template_name= 'main/contact_information.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Techking - Контактная иформация'
        return context


class PaymentDeliveryView(TemplateView):
    template_name= 'main/payment_delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Techking - Доставка и оплата'
        return context
    

class AboutView(TemplateView):
    template_name= 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Techking - О нас'
        return context