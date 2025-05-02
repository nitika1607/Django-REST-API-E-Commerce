from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views  
from .views import product_list_api, product_detail_api


urlpatterns = [
    path('', views.index, name='index'),
    path('product-page/', views.product_page, name='product_page'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('products/', product_list_api, name='product-list-api'),
    path('products/<int:pk>/', product_detail_api, name='product-detail-api'),
    
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
     path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='reset_password'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('client/', views.client, name='client'),
   

]
