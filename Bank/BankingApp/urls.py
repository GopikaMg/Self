from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('application/',views.application,name='application'),
    path('cities/',views.cities,name='cities'),
    path('sample/',views.sample,name='sample'),
    path('accept/', views.accept, name='accept'),


    ]