from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from .models import *
from django import forms
from django.forms import ModelForm
import json
# Create your views here.

# Forms begin


class reg(forms.Form):
    name = forms.CharField()
    mobile = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)
    pwdAgn = forms.CharField(label='Password Again', widget=forms.PasswordInput)
    role = forms.CharField(widget=forms.Select(choices=(('Retailer', 'Retailer'), ('Customer', 'Customer'))))
    email = forms.CharField(widget=forms.EmailInput)


class productForm(ModelForm):

    class Meta:
        model = Products
        fields = '__all__'

# Forms end


def userLogin(request):
    if request.method == 'GET':
        response = {
            'msg': "Login",
            'method': "GET"
        }
        return render(request, 'home/login.html', response)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mem = Member.objects.get(mobile=username)
        print(mem)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("user",mem.name);
            if mem.role == "Retailer":
                response = {
                    'msg': mem.name,
                    'method': 'GET'
                }
                return redirect('/retailer/dashboard/')
            elif mem.role == "Customer":
                return redirect('/')
        else:
            return redirect('/login/')


def home_page(request):
    if request.user.is_authenticated():
        mem = Member.objects.get(username=request.user.username)
        response = {
            'msg': 'Welcome '+mem.name
        }
    else:
        response = {
            'msg': 'Welcome'
        }
    return render(request, 'home/showProducts.html', response)


def userLogout(request):
    logout(request)
    # response = {
    #     'msg': 'Welcome'
    # }
    return redirect('/')


def register(request):
    response = {
        'msg': 'Register here'
    }
    if request.method == 'GET':
        f = reg()
        print(f.as_table());
        response.update({
            'method': 'GET',
            'msg': 'Register Here',
            'form': f.as_table()
        })
        return render(request, 'home/registration.html', response)
    if request.method == 'POST':
        form = reg(request.POST)
        if form.is_valid():
            mem = Member()
            try:
                mem = Member.objects.get(username=form.cleaned_data['mobile'])
                f = reg()
                response.update({
                    'method': 'GET',
                    'msg': 'Mobile number has already been registered!!',
                    'form': f.as_table()
                })
                return render(request, 'home/registration.html', response)
            except Exception:
                mem.name = form.cleaned_data['name']
                mem.mobile = form.cleaned_data['mobile']
                mem.username = form.cleaned_data['mobile']
                mem.role = form.cleaned_data['role']
                if len(form.cleaned_data['password']) < 8:
                    f = reg()
                    response.update({
                        'method': 'GET',
                        'msg': 'Weak password!!',
                        'form': f.as_table()
                    })
                    return render(request, 'home/registration.html', response)
                if form.cleaned_data['password'] != form.cleaned_data['pwdAgn']:
                    f = reg()
                    response.update({
                        'method': 'GET',
                        'msg': 'Password mismatch!!',
                        'form': f
                    })
                    return render(request, 'home/registration.html', response)
                mem.pwd = form.cleaned_data['password']
                mem.set_password(mem.pwd)
                mem.email_id = form.cleaned_data['email']
                mem.email = mem.email_id
                mem.save()
                response.update({
                    'msg': 'Registration Successful'
                })
                return render(request, 'home/home_page.html', response)
        else:
            f = reg()
            response.update({
                'method': 'GET',
                'msg': 'Fill valid data!!',
                'form': f.as_table()
            })
            return render(request, 'home/registration.html', response)


def showProducts(request):
    return render(request, 'home/showProducts.html', {})


# APIs start


@csrf_exempt
def removeProduct(request):
    response = {'msg': 'Success'}
    # print(request.GET['category'])
    # print(jsonRequest)
    json_request = json.loads(request.body)
    productId = json_request.get('productId')
    try:
        pro = Products.objects.get(id=int(productId))
        pro.delete()
    except Exception as e:
        response.update({'msg': 'Error in removing product'})
        print(e)
    return JsonResponse(response)

# @csrf_exempt
# def getCategories(request):
#     response = {'msg': 'Success'}
#     categoryList = []
#     try:
#         categories = Category.objects.all()
#         for c in categories:
#             categoryList.append(c.name)
#         response.update({'categoryList': categoryList})
#     except Exception as e:
#         response.update({'msg': 'Error in fetching categories'})
#         print(e)
#     return JsonResponse(response)

# APIs end