from django.contrib import admin
from django.urls import path
from myapp import views
app_name = 'myapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('book/<int:book_id>/',views.detail,name='detail'),
    path('add/',views.add_book, name='add_book'),
    path('update/<int:id>/', views.update, name ='update'),
    path('delete/<int:id>/', views.delete, name = 'delete'),
    path('register/', views.registerpage, name = 'register'),
    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.logoutuser, name = 'logout'),
]
