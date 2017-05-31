from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from .views import *
from .api import *

v1_api = Api(api_name='v1')
v1_api.register(ProductResource())
v1_api.register(CategoryResource())

urlpatterns = [
    url(r'^$', home_page),
    url(r'^register/$',register),
    url(r'^login/$',userLogin),
    url(r'^logout/$',userLogout),
    url(r'^showProducts/$',showProducts),
    url(r'^removeProduct/$',removeProduct),

    # url(r'^api/getCategoryProducts/$',getCategoryProducts),
    # url(r'^api/getCategories/$',getCategories),
    url(r'^api/', include(v1_api.urls)),

]
