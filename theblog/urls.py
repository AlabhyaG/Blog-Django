from django.urls import path,include
from . views import *


urlpatterns=[
    path('',HomeView,name='Home'),
    path('blog/<int:pk>/',DetailView,name='detail_blog'),
    path('createblog/',PostCreateView,name='create-post'),
    path('editblog/<int:pk>/',PostEditView,name='edit-post'),
    path('delete_post/<int:pk>/',DeletePostView,name='delete-post'),
]