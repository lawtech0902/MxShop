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
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")

# 配置category的url
router.register(r'categorys', CategoryViewset, base_name="categorys")

# 配置code的url
router.register(r'codes', SmsCodeViewset, base_name="codes")

# 配置users的url
router.register(r'users', UserViewset, base_name="users")

# 配置userfav的url
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'^', include(router.urls)),

    url(r'docs/', include_docs_urls(title='慕学生鲜')),

    url(r'^api-token-auth/', views.obtain_auth_token),

    url(r'^login/', obtain_jwt_token)
]
