#coding:utf-8
from django.shortcuts import render
from django.shortcuts import  render_to_response
# Create your views here.
import json
from django.http.response import HttpResponse
data={
      'shandong':{
                  'jinan':['A','B','C'],
                  'dechou':['paji','BN','CI'],
                  },
      'hebei':{
                  'shijiaz':['A','B','C'],
                  'baoding':['AA','BB','CC'],
                  'chengde':[ 'AAA','BBB','CCC']
                  },
    }
def Index(request):
    return render_to_response('Index.html')
def GetProvince(request):
    result=data.keys() 
    return HttpResponse(json.dumps(result))
def GetCity(request):
    getData=request.GET
    proviceId=getData.get('Id')
    #将所有值全部取出
    result=data.values()
    #根据省的iD取出对应的市
    result2=result[int(proviceId)]
    result3=result2.keys()
    return HttpResponse(json.dumps(result3))
def GetCounty(request):
    getData=request.GET
    #获取值  
    proviceId=getData.get('proId')
    cityId=getData.get('cityId')
    #将所有值全部取出
    result=data.values()
    #根据省的iD取出对应的市
    result2=result[int(proviceId)]
    result3=result2.values()
    result4=result3[int(cityId)]
    return HttpResponse(json.dumps(result4))
    