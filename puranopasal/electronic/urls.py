from django.urls import path
from . import views


urlpatterns=[
    path('',views.elect,name='elect'),
    path('laptops/', views.laptop_list, name='laptop_list'),
    path('headphone/', views.headphone_list, name='headphone_list'),
    path('iron/', views.iron_list, name='iron_list'),
    path('microoven/', views.microoven_list, name='microoven_list'),
    path('mobile/', views.mobile_list, name='mobile_list'),
    path('refrigerator/', views.refrigerator_list, name='refrigerator_list'),
    path('speaker/', views.speaker_list, name='speaker_list'),
    path('tv/', views.tv_list, name='tv_list'),
    path('vaccum/', views.vaccum_list, name='vaccum_list'),
    path('search/', views.search_list, name='search_list'),



]