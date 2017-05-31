from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from .views import *
from home.api import *


v1_api = Api(api_name='v1')
v1_api.register(ProductResource())
v1_api.register(CategoryResource())

urlpatterns = [
    url(r'^dashboard/$', dashboard),
    url(r'^(?P<product_id>[0-9]+)/(?P<category_id>[0-9]+)/editProduct/$', editProduct),
    url(r'^addProduct/$',addProduct.as_view()),
    url(r'^api/', include(v1_api.urls)),

]