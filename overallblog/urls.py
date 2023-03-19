from django.urls import path , include
from .views import *

urlpatterns = [
    path('blog',index,name='indexpage'),
    path('home',home,name='homepage'),
    path('login_page',login_route,name="loginpage"),
    path('logout_page',userlogout,name="userlogout"),
    path('edituser',edituser,name="edituser"),
    path("addblog",addblog,name="addblog"),
    path('delete/<int:id>/',Blog_delete),
    path('update/<int:id>/',Blog_update),
    # path('das',dashboard,name="dashboard"),
]