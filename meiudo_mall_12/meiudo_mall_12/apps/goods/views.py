from django.shortcuts import render

# Create your views here.
from drf_haystack.serializers import HaystackSerializer

from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from goods.models import SKU
from goods.search_indexes import SKUIndex
from users.serializers import SKUSerializer


class SKUListView(ListAPIView):
    """
    sku列表数据
    """
    serializer_class = SKUSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('create_time', 'price', 'sales')

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return SKU.objects.filter(category_id=category_id, is_launched=True)


class SKUIndexSerializer(HaystackSerializer):
    """
    SKU索引结果数据序列化器
    """

    class Meta:
        index_classes = [SKUIndex]
        fields = ('text', 'id', 'name', 'price', 'default_image_url', 'comments')
