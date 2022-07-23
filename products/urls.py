from django.urls import path
from . import ajax_view, views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.order_create, name='order_create'),
    path('<category>/', views.product_category, name='product_category'),
    path('<slug:category_slug>/', views.product_category, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('pay-with-paystack/', ajax_view.AjaxPayment.as_view(), name='pay_with_paystack'),
    path('ajax-payment/', views.ajax_payment, name='ajax_payment'),
    path('<int:id>/pdf', views.Pdf.as_view(), name='render_pdf'),
    path('save-billing/', ajax_view.SaveBilling.as_view(), name='save_billing'),
]








# redis:
#         image: redis:5-alpine
#         networks:
#             - kip-homes

#     celery_worker:
#         build:
#             context: .
#             dockerfile: ./docker/local/django/Dockerfile
#         command: /start-celeryworker
#         volumes:
#             - .:/app
#         env_file:
#             - .env
#         depends_on:
#             - redis
#             - postgres-db
#         networks:
#             - kip-homes

#     flower:
#         build:
#             context: .
#             dockerfile: ./docker/local/django/Dockerfile
#         command: /start-flower
#         volumes:
#             - .:/app
#         env_file:
#             - .env
#         ports:
#             - "5557:5555"
#         depends_on:
#             - redis
#             - postgres-db
#         networks:
#             - kip-homes

#     nginx:
#         restart: always
#         depends_on:
#             - api
#         volumes:
#             - static_volume:/app/staticfiles
#             - media_volume:/app/mediafiles
#         build:
#             context: ./docker/local/nginx
#             dockerfile: Dockerfile
#         ports:
#             - "8080:80"
#         networks:
#             - kip-homes
