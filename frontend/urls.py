from django.urls import path, include
from frontend import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
]
