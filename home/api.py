from tastypie.resources import ModelResource,ALL_WITH_RELATIONS
from tastypie import fields
from .models import *


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        filtering = {
            'name': ALL_WITH_RELATIONS,
            'id': ALL_WITH_RELATIONS
        }


class ProductResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category')
    class Meta:
        queryset = Products.objects.all()
        filtering = {
            'category': ALL_WITH_RELATIONS
        }
