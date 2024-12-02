# employee_register/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/update/<int:id>/', views.employee_update, name='employee_update'),
    path('employee/delete/<int:id>/', views.employee_delete, name='employee_delete'),
]
