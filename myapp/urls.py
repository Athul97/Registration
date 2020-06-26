from django.urls import path
from . import views

urlpatterns = [
    path('index', views.fn_index),
    path('adminlog/', views.fn_adminLog),
    path('register/', views.fn_reg),
    path('empreg/', views.fn_empreg),
    path('reg_log/', views.fn_reglog),
    path('trash/', views.fn_trash),
    path('edit/', views.fn_edit),
    path('editprofile/', views.fn_editprofile),
]
