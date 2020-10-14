from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_image, name='search_image'),
    path('location/<location_name>/', views.imageLocation, name='imageLocation'),
    path('image/<category_name>/<int:image_id>',views.single,name = 'single')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)