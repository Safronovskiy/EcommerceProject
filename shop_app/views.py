from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import ProductModel, CategoryProductModel, CartProductModel
from .forms import AddCategoryProductForm

# def startpage(request):
#     return render(request, 'startpage.html')




class ProductListView(ListView):
    model = ProductModel
    template_name = 'startpage.html'
    context_object_name = 'products'  # default value='object_list'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = CategoryProductModel.objects.all()
        return context

    def get_queryset(self):
        return ProductModel.objects.all()

class ProductCategoryView(ListView):
    model = ProductModel
    template_name = 'startpage.html'
    context_object_name = 'products'  # default value='object_list'
    allow_empty = False    #при отсутствии категории выдаёт 404


    def get_queryset(self):
        return ProductModel.objects.filter(category=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = CategoryProductModel.objects.all()
        return context

class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product_details.html'
    slug_url_kwarg = 'prod_slug'
    context_object_name = 'product'

    def get_queryset(self):
        return ProductModel.objects.filter(product_slug=self.kwargs['prod_slug'])


class AddCategoryProductView(CreateView):
    form_class = AddCategoryProductForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('/')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = CategoryProductModel.objects.all()
        return context


























