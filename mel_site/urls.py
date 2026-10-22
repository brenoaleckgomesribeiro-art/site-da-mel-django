from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('historias/', views.historias, name='historias'),
    path('novidades/', views.novidades, name='novidades'),
]