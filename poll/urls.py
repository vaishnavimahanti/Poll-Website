from django.urls import path
from poll import views


urlpatterns = [
	path('', views.start, name="logout"),
	path('user/', views.userPage, name="user-page"),
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
    path('home/', views.home, name="home"),
] 