from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from goods.utils import q_search
from goods.models import Products

def custom_404_view(request, exception):
    return render(request, "404.html", {"message": str(exception)}, status=404)

class CatalogView(ListView):
    model = Products
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 3
    allow_empty = False

    def get_queryset(self):

        category_slug = self.kwargs.get("category_slug")
        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")

        if category_slug == 'all':
            goods = super().get_queryset()
        elif query:
            goods = q_search(query)
            if not goods.exists():
                raise Http404("К сожалению, у нас нет такого товара")
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)
            if not goods.exists():
                raise Http404()

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)

        return goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "TechKing - Каталог"
        context['slug_url'] = self.kwargs.get("category_slug")
        return context
    

class ProductView(DetailView):
    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset = None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context