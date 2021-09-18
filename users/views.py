import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    """访问首页的视图"""
    # return HttpResponse("hello django")
    # render返回的是HttpResponse对象
    return render(request, 'index.html')


def hello(request, a, b):
    return HttpResponse("模块%s，页面%s" % (a, b))


def new2(request):
    category = request.GET.get('category')
    page = request.GET.get('page')
    text = "获取查询字符串category = %s,page = %s" % (category, page)
    return HttpResponse(text)


def new3(request):
    category = request.POST.get('category')
    page = request.POST.get('page')
    text = "获取请求中的键值对 category = %s page = %s" % (category, page)
    return HttpResponse(text)


def new4(request):
    # 获取json字符串
    json_data = request.body
    # 解析json数据
    json_dict = json.loads(json_data)
    category = json_dict.get('category')
    page = json_dict.get('page')
    text = "获取请求体中的键值对 category = %s page = %s" % (category, page)
    return HttpResponse(text)


def resp(request):
    response = HttpResponse(content="首页", status=201)
    response["category"] = 20
    response["page"] = 30

    return response


def resp1(request):
    respones = JsonResponse([{"name": "老王", "age": 18, "hobby": "table tennis"},
                             {"name": "老张", "age": 20, "hobby": "basketball"}
                             ], safe=False, json_dumps_params={'ensure_ascii': False}, status=200) # json_dumps_params={'ensure_ascii': False} 解决返回中文乱码问题

    return respones


def my_redirect(requests):
    return redirect('/index')


def my_redirect1(request):
    url = reverse('users:resp1')
    return redirect(url)

