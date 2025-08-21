from django.urls import path
from . import views


urlpatterns=[
    path('',views.signup,name='signup'),
    path('', views.success_view, name='success_page'),

]