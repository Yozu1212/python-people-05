from django.contrib import admin
from django.urls import path
from mysite import views     # 從views.py去匯入所有的處理函式

urlpatterns = [
    path('areaperson/', views.areaperson_data),         # 村里人口統計
    path("citypeople/", views.citypeople_data), 
    path('', views.index ),  # 如果有人來瀏覽首頁的話，請交給views.py裡面的index()函式處理
    path("born/", views.born_data),
    path('admin/', admin.site.urls),
    path("tpchart/", views.tpchart_data),
    path("ntchart/", views.ntchart_data),
    path("tychart/", views.tychart_data),
    path("tcchart/", views.tcchart_data),
    path("tnchart/", views.tnchart_data),
    path("kschart/", views.kschart_data),#高雄
    path("ALLIN/", views.allin_data),#高雄
]

