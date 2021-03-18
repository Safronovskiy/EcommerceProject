from django.urls import path
from .views import *



app_name='shop_app'

urlpatterns = [
    # path('', startpage, name='start'),
    path('', ProductListView.as_view(), name='start'),
    path('category/<slug:cat_slug>/', ProductCategoryView.as_view(), name='category'),
    path('product_details/<slug:prod_slug>/', ProductDetailView.as_view(), name='details'),
    path('add_category/', AddCategoryProductView.as_view(), name='add_category'),

]

