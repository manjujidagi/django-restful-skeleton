# ------ Type - 2 -------------
from django.urls import path
from users import views

urlpatterns = [
    path('', views.users_list),
    path('<int:pk>/', views.user_detail),
    path('login/', views.user_login),
]