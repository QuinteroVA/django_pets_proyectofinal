from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('booking/', views.booking, name="booking"),
    path('single/', views.single, name="single"),
]