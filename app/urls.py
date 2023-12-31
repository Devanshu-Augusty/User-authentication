from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="home"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]