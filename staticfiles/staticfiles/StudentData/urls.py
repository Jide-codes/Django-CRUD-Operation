from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show, name="home"),
    path('<int:pk>/', views.delete_data, name="delete_data"),
     path('update_data/<int:pk>/', views.update_data, name="update_data")
]
