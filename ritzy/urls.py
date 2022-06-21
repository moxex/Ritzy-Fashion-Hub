from django.urls import path
from . import views

app_name = 'ritzy'

urlpatterns = [
    path('', views.home, name='ritzy-home'),
    path('about/', views.about, name='ritzy-about'),
    path('contact_us/', views.contact_us, name='ritzy-contact'),
]