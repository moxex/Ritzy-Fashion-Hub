from django.urls import path
from . import ajax_view, views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.order_create, name='order_create'),
    path('<category>/', views.product_category, name='product_category'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('ajax_payment/', views.ajax_payment, name='ajax_payment'),
    path('pay_with_paystack/', ajax_view.AjaxPayment.as_view(), name='pay_with_paystack'),
    path('<int:id>/pdf', views.Pdf.as_view(), name='render_pdf'),
]