from django.urls import path
from . import views

app_name='shop'

urlpatterns=[

    path('list/',views.products_list,name='products_list'),
    path('<slug:category_slug>/',views.products_list,name='products_list'),
    path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail')

    ]
