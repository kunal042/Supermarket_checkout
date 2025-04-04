from django.shortcuts import render

from django.http import JsonResponse
from .cart import calculate_total

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ProductSerializer
from .models import Product


# def checkout_view(request):
#     cart_items = request.GET.get("items", "")
#     total_price = calculate_total(cart_items)
#     return JsonResponse({"total_price": total_price})



# get calacuated the total price where product is selected


class CheckoutAPIView(APIView):
    def get(self, request):
        cart_items = request.query_params.get("items", "")
        total_price = calculate_total(cart_items)
        return Response({"total_price": total_price}, status=status.HTTP_200_OK)


# POST Api where we add product 
class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET all Product availiable  
class ProductListView(APIView):
    def get(self, request):
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


