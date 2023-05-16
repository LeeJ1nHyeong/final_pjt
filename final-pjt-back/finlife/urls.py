from django.urls import path
from . import views

app_name = 'finlifes'
urlpatterns = [
    # path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),
    # path('deposit-product-options/<fin_prdt_cd>/', views.deposit_product_options),
    # path('deposit-products/top-rate/', views.top_rate),
]