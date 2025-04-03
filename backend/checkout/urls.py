from django.urls import path
from .views import  CheckoutAPIView, ProductCreateView,ProductListView

urlpatterns = [
    path("checkout/", CheckoutAPIView.as_view(), name="checkout"),
    path('products/', ProductCreateView.as_view(), name='product-create'),
    path('productList/', ProductListView.as_view(), name='product-list'),


]
