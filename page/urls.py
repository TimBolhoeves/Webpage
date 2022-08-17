from django.urls import path
from . import views

urlpatterns = [
    # home page
    path('', views.index, name='index'),

    # auth
    path('login/', views.login, name='login'),
    path('login/post/', views.loginpost, name='loginpost'),
    path('logout/', views.logout, name='logout'),
    #----

    #CRUD
    path('additem/', views.additem, name='additem'),
    path('additem/add/', views.add, name='add'),

    path('deleteitem/<int:id>', views.deleteitem, name='deleteitem'),

    path('updateitem/<int:id>', views.updateitem, name='updateitem'),
    path('updateitem/update/<int:id>', views.update, name='update'),

    path('updateimage/<int:id>', views.updateimage, name='updateimage'),
    path('updateimage/updateimg/<int:id>', views.updateimg, name='updateimg'),
    #----

]