from django.urls import path
from .import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('aboutpage', views.aboutpage, name='aboutpage'),

    path('usercreate', views.usercreate, name='usercreate'),
    path('loginp', views.loginp, name='loginp'),
    path('logout', views.logout, name='logout'),
    path('adminhome', views.adminhome, name='adminhome')
]