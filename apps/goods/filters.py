# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/11/27 上午9:26'
"""

from django_filters import rest_framework as filters

from .models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    price_min = filters.NumberFilter(name="shop_price", lookup_expr="gte")
    price_max = filters.NumberFilter(name="shop_price", lookup_expr="lte")

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']
