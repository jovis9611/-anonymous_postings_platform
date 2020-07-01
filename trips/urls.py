from django.urls import path
from .views import home
from . import views

app_name = 'trips'

urlpatterns = [
    
    path(r'', home,name='home'),
    path(r'post/<pk>/', views.post_detail, name='post_detail'),
    path(r'^post/new/$', views.post_new, name='post_new'),
    path(r'post_edit/', views.post_edit, name='post_edit'),

]