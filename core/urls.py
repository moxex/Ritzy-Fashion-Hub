from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ritzy.urls')),
    path('products/', include('products.urls', namespace='product')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('blog/', include('posts.urls', namespace='post')),
    path('accounts/', include('accounts.urls', namespace='account')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Ritzy Fashion Admin'
admin.site.site_title = 'Ritzy Fashion Admin Portal'
admin.site.index_title = 'Welcome to the Ritzy Fashion Portal'
