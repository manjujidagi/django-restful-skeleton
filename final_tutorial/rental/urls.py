# ------ Type - 2 -------------
from django.urls import path
from rental import views

urlpatterns = [
    path('friends/', views.friends_list),
]