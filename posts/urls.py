from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/<str:slug>/', views.post_detail, name='post_detail'),
    path("<category>/", views.post_category, name="post_category"),
]