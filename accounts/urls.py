from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('postad', views.postad, name='post'),
    path('dashboard', views.dashboard, name='dashboard'),
 	path('delete/<int:list_id>', views.delete, name='delete')
       
]

