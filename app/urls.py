from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Home, name='index'),
    path('complain', views.Form, name='complain'),
    path('report', views.ReportView, name='report')
]
