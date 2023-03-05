from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('posts/', views.posts, name='posts'),
    path('jobs/', views.jobs, name='jobs'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('add_student/', views.add_student, name='add_student'),
    path('store_student/', views.store_student, name='store_student'),

]
