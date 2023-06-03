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
    # 先把舊資料通通刪除
    models.HBicycleData.objects.all().delete()
    # 要比照all_data函式的程式，把網站上所有的資料都下載解析，放到資料表 (HBicycleData) 裡面
    url = "https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"
    r = requests.get(url)         
    data = json.loads(r.text)     
    bicycle_data = data['retVal'] 
    for item in bicycle_data:
        new_record = models.HBicycleData(
            sna = item['sna'].split("_")[1],
            sbi = int(item['sbi']),
            tot = int(item['tot'])
            )
        new_record.save()

    # 過濾 HBicycleData 裡面的所有記錄，找出其中sbi>=10的站台放到data中
    data = models.HBicycleData.objects.filter(sbi__gte=10)
    return render(request, "filter.html", locals())

def chart(request):
    data = models.PhoneModel.objects.all()
    return render(request, "chart.html", locals())

def stock300list(request):
    data = models.StockInfo.objects.filter(price__gte=300).order_by('-price')
    numbers = len(data)
    return render(request, "stocklist.html", locals())