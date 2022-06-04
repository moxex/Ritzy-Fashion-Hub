from django.urls import path
from . import views

app_name = 'ritzy'

urlpatterns = [
    path('', views.home, name='ritzy-home'),
]