from product.models import Product
from product.serializers import ProductDetailSerializer, ProductListSerializer
from rest_framework import generics, mixins
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
        product_list = Product.objects.filter(name__startswith=alphabet)
        print(product_list)
        return Response({
            'product_list': ProductListSerializer(product_list, many=True).data,
        }, status=status.HTTP_200_OK)
    
    # def get_queryset(self, alphabet):
    #     return 

class ProductDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)