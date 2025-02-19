from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name= 'main/index.html'

    # def get(self, request, *args, **kwargs):
    #     print('something interesting')
    #     return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home - Главная'
        context["content"] = 'Магазин мебели HOME'
        # context['categories'] = Categories.objects.all()
        return context
    


class AboutView(TemplateView):
    template_name= 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home - О нас'
        context["content"] = 'О нас'
        context["text_on_page"] = 'Что-то там очень интересное'
        return context
# def index(request):

#     context = {
#     'title': 'Home - Главная',
#     'content': 'Магазин мебели HOME'
#     }

#     return render(request, 'main/index.html', context)

# def about(request):
#     context = {
#     'title': 'Home - О нас',
#     'content': 'О нас',
#     'text_on_page': 'Что-то там очень интересное'
#     }

#     return render(request, 'main/about.html', context)

