from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_image, name='search_image'),
    path('location/<location>', views.location_filter, name='location_filter'),
    path(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single,name = 'single')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)