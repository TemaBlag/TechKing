from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name= 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home - Главная'
        context["content"] = 'Магазин мебели HOME'
        return context
    


class AboutView(TemplateView):
    template_name= 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home - О нас'
        context["content"] = 'О нас'
        context["text_on_page"] = 'Что-то там очень интересное'
        return context