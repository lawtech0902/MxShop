"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

import DjangoUeditor
import xadmin

from goods.views import GoodsListViewSet, CategoryViewset, BannerViewset, HotSearchsViewset, IndexCategoryViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView

router = DefaultRouter()

# 配置goods的url(商品)
router.register(r'goods', GoodsListViewSet, base_name="goods")

# 配置category的url(商品种类)
router.register(r'categorys', CategoryViewset, base_name="categorys")

# 配置code的url(验证码)
router.register(r'codes', SmsCodeViewset, base_name="codes")

# 配置users的url(用户)
router.register(r'users', UserViewset, base_name="users")

# 配置userfavs的url(收藏)
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

# 配置messages的url(留言)
router.register(r'messages', LeavingMessageViewset, base_name="messages")

# 配置address的url(收货地址)
router.register(r'address', AddressViewset, base_name="address")

# 配置shopcarts的url(购物车)
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")

# 配置orders的url(订单)
router.register(r'orders', OrderViewset, base_name="orders")

# 配置hotsearchs的url(热搜)
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")

# 配置banners的url(轮播图)
router.register(r'banners', BannerViewset, base_name="banners")

# 配置indexgoods的url(首页商品系列数据)
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^', include(router.urls)),
    url(r'docs/', include_docs_urls(title='慕学生鲜')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^login/$', obtain_jwt_token),
    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),
    # 第三方登录url
    url('', include('social_django.urls', namespace='social'))
]
