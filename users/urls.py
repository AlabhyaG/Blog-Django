from django.urls import path
from . views import *
urlpatterns=[
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),
    path('register/',registerView,name='register'),
    path('profile/<int:pk>/',profileView,name='profile'),
    path('<int:pk>/edit-profile/',profileUpdateView,name='profile-update')

]
