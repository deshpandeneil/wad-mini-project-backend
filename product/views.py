from product.models import Product
from product.serializers import ProductListSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class ProductList(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    http_method_names = ['post']
    permission_classes = [AllowAny]

    # def get_serializer(self, instance=None, data=None, many=False, partial=False):
    #     return super(ProductList, self).get_serializer(instance=instance, data=data, many=True, partial=partial)

    def post(self, request, *args, **kwargs):
        alphabet = request.data.get('alphabet', 'A').upper()
        print("ALPHABET IS: ", alphabet)
        product_list = Product.objects.filter(disease_category_fk__name__startswith=alphabet)
        print(product_list)
        return Response({
            'product_list': ProductListSerializer(product_list, many=True).data,
        }, status=status.HTTP_200_OK)
    
    # def get_queryset(self, alphabet):
    #     return 
