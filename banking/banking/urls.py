from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('customer/', views.customer),
    path('trans/', views.trans),
    path('transfer/', views.transfer),
    path('add/', views.add),
    path('send/', views.send),
    path('delete/', views.delete),
    path('admin/', admin.site.urls),
]
