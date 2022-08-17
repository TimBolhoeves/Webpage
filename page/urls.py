from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/post/', views.loginpost, name='loginpost'),
    path('logout/', views.logout, name='logout'),
    path('additem/', views.additem, name='additem'),
    path('additem/add/', views.add, name='add'),
    path('deleteitem/<int:id>', views.deleteitem, name='deleteitem'),
]