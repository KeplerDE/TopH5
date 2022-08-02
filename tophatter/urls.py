from django.urls import path
from . import views


app_name = 'TopH'

urlpatterns = [
    path('', views.home, name='home'),
    path('/abo', views.about, name='about'),
    path('/services/', views.services, name='services'),

]
