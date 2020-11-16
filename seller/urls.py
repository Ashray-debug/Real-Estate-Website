from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name="slogin"),
    path('logout', views.logout, name='slogout'),
    path('dashboard', views.dashboard, name='sdashboard')
]