from django.urls import path, include
from ecomm import views


urlpatterns = [
    path("products/<pk>", views.ProductDetailAPI.as_view()),
    path("products", views.ProductListAPI.as_view()),
]
