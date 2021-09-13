# -*- coding: UTF-8 -*-
# @Time     : 2021/8/26 14:55
# @Author   : liangyaqiong
# @File     : views.py
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from TestModel.models import TbUiElementInfo
import  json


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)


def testdb(request):
    test = TbUiElementInfo(id=423,name='test_button',page='test_page')
    test.save()
    return HttpResponse("<p>数据添加成功！</p>")

def testquery(request):
    listdata = TbUiElementInfo.objects.get_elms_by_component(component_name='logout_dialog', page_name='settings')
    serialized_q = serializers.serialize('json', listdata, ensure_ascii=False)
    print(serialized_q)
    return HttpResponse(serialized_q)

def testqueryall(request):
    listdata = TbUiElementInfo.objects.all().order_by('id')
    # 将QuerySet转换成json
    serialized_q = serializers.serialize('json', listdata, ensure_ascii=False)
    return HttpResponse(serialized_q)

# def testquerybyid(request):
#     ids = request.GET.get('id')
#     listdata = TbUiElementInfo.objects.get_elm_by_id(ids)
#     # 将QuerySet转换成json
#     serialized_q = serializers.serialize('json', listdata, ensure_ascii=False)
#     return HttpResponse(serialized_q)

def testdelete(request):
    id = request.GET.get('id')
    if id:
       TbUiElementInfo.objects.delete_elms_by_id(id)
       response = '已删除数据'+id
       return HttpResponse(response)
    else:
       return HttpResponse('error！')

