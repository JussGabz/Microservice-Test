from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .producer import publish
from .models import Product, User
from .serializers import ProductSeralizer

import random

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSeralizer(products, many=True)
        return Response(serializer.data)
         

    def create(self, request):
        # Get JSON and Serialize data
        serializer = ProductSeralizer(data=request.data)
        print(request.data)
        serializer.is_valid()
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        # Search for Object by ID 
        product = Product.objects.get(id=pk)
        serializer = ProductSeralizer(instance=product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        # Grab existing Product by ID
        product = Product.objects.get(id=pk)

        # Serialize existing Product Instance w/ request data 
        serializer = ProductSeralizer(instance=product, data=request.data)

        # Check Validity & Save
        serializer.is_valid()
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        # Find Product by ID 
        product = Product.objects.get(id=pk)
        # Delete/Destroy
        product.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })