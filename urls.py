from django.urls import path

from . import views

app_name = 'otbank'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:pk>/', views.ConstraintView.as_view(), name='constraint'),
]