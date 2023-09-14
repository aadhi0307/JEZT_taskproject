"""jezt_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashboard,name="dashboard"),
    path('todo_data/',views.todo_data,name="todo_data"),
    path('todo_delete/<int:dataid>/',views.todo_delete,name="todo_delete"),
    path('reminder_add/',views.reminder_add,name="reminder_add"),
    path('reminder_delete/<int:dataid>/',views.reminder_delete,name="reminder_delete"),
    path('get_weather/',views.get_weather,name="get_weather"),
    

    
]
