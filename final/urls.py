
from django.contrib import admin
from django.urls import path
import fina.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',fina.views.home, name='home'),
    path('/writes/', fina.views.writes, name='writes'),
    path('/create/', fina.views.create, name='create'),
    path('/modify/<int:fina_id>', fina.views.modify, name='modify'),
    path('/delete/<int:fina_id>',fina.views.delete, name="delete"),
    path('/<int:fina_id>/', fina.views.detail, name ='detail'),
    path('/pictur/', fina.views.pictur, name ='pictur'),
    path('/login/', fina.views.login, name ='login'),
    path('/lecture/', fina.views.lecture, name ='lecture'),
    path('/board/', fina.views.board, name ='board'),
]
