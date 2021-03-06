from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from home.models import *
from home.views import *
import pdb
# Create your views here.


def dashboard(request):
    if request.user.is_authenticated():
        mem = Member.objects.get(username=request.user.username)
        return render(request, 'retailer/dashboard.html', {'msg': "Welcome "+mem.name})
    else:
        return redirect('/login/')


def editProduct(request, product_id):
    if request.method == 'GET':
        if request.user.is_authenticated():
            mem = Member.objects.get(username=request.user.username)
            response = {
                'msg': "Welcome "+mem.name,
                'method': 'GET',
            }
            return render(request,'retailer/editProduct.html',response)
        else:
            return redirect('/login/')
    if request.method == 'POST':
        print(request.POST['image'])
        pro = Products.objects.get(id=int(product_id))
        pro.name = request.POST['name']
        pro.price = request.POST['price']
        if(request.POST['image']):
            pro.image = request.POST['image']
        pro.category = Category.objects.get(id=int(request.POST['category']))
        pro.save()
        return redirect('/retailer/dashboard')


class addProduct(View):
    response = {
        'method': 'GET',
        'addProductMsg': 'Add Product'
    }

    def get(self, request):
        if request.user.is_authenticated():
            mem = Member.objects.get(username=request.user.username)
            form = productForm()
            print(form.as_table())
            self.response.update({
                'msg': "Welcome "+mem.name,
                'method': 'GET',
                'addProductMsg': 'Add Product',
                'form': form,
            })
            return render(request, 'retailer/addProduct.html', self.response)

    def post(self, request):
        print("inside")
        form = productForm(request.POST, request.FILES)
        new_form = productForm()
        print(new_form)
        if form.is_valid():
            product = form.save()
            self.response.update({
                'addProductMsg': 'Product added Successfully',
                'method': 'GET',
                'form': new_form
            })
            return render(request, 'retailer/addProduct.html', self.response)
        else:
            self.response.update({
                'addProductMsg': 'Invalid Input',
                'method': 'GET',
                'form': new_form
            })
            return render(request, 'retailer/addProduct.html', self.response)
