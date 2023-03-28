import base64
from .models import * 
from rest_framework import generics
from .serializers import * 
# from PIL import Image 
from django.db.models import Q

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(Q(name__contains = search) | Q(category__contains = search) | Q(brand_name__contains = search))
        return queryset

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'