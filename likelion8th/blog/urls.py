from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name = "detail"),
    path('new', views.new, name = "new"),
    path('create', views.create, name = "create"),
    path('edit/<int:blog_id>', views.edit, name = "edit"), #id값 받아야되니까 <int:blog_id>패스커먼드? 써줘
    path('update/<int:blog_id>', views.update, name = "update"),
    path('delete/<int:blog_id>', views.delete, name = "delete"),
    path('commenting/<int:blog_id>', views.commenting, name='commenting'),
    path('like/<int:blog_id>', views.like, name='like'),
]