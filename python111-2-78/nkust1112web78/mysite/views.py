from django.shortcuts import render   # 渲染網頁
from django.http import HttpResponse   # Django用來回應給瀏覽器特定資料的函式
import requests   # 匯入擷取網頁所需要的模組
import json       # 匯入操作JSON格式所需要的模組
from mysite import models  # 從 mysite 的資料夾中的 models.py 匯入所有的類別（資料表）
import random     # 匯入隨機模組

def index(request):
    myname = "第五組"
    return render(request, "index.html", locals())

def nkustnews(request):
    data = models.NKUSTnews.objects.all()
    return render(request, "nkustnews.html", locals())

def phonelist(request, id=-1):
    if id == -1:
        data = models.PhoneModel.objects.all()              #找出所有的手機
    else:
        maker = models.PhoneMaker.objects.get(id=id)        #找出一個(get)指定的廠牌
        data = models.PhoneModel.objects.filter(maker=maker) #找出一堆(filter)符合的資料
    return render(request, "phonelist.html", locals())

def all_data(request):
    url = "https://www.ris.gov.tw/rs-opendata/api/v1/datastore/ODRP012/10701"
    r = requests.get(url)         
    data = json.loads(r.text)   
    peopledata = data['responseData']  
    msg = ""
    msg = "<center><h2>人口統計資料</h2><center><hr>"  
    msg = msg + "<center><table><tr bgcolor=#aaaaaa><td>地區</td><td>村里名稱</td><td>戶數</td><td>總人口</td><td>男</td><td>女</td><td>總出生人數</td><td>死亡人數(男)</td><td>死亡人數(女)</td></tr>"
    for item in peopledata:
        msg = msg + "<tr bgcolor=#33ff33><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
            item['site_id'],
            item['village'], 
            item['household_no'],
            item['people_total'],
            item['people_total_m'],
            item['people_total_f'],
            item['birth_total'],
            item['death_m'],
            item['death_f']
            )
    msg = msg + "</table></ccenter>"
    return HttpResponse(msg)

def filtered_data(request):
    return render(request, "filter.html", locals())

    data = models.StockInfo.objects.filter(price__gte=300).order_by('-price')
    numbers = len(data)
    return render(request, "filter.html", locals())


def chart(request):
    data = models.PhoneModel.objects.all()
    return render(request, "chart.html", locals())

def stock300list(request):
    data = models.StockInfo.objects.filter(price__gte=300).order_by('-price')
    numbers = len(data)
    return render(request, "stocklist.html", locals())

def born_data(request):
    data = models.StockInfo.objects.filter(price__gte=300).order_by('-price')
    numbers = len(data)
    return render(request, "born.html", locals())