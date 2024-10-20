from django.urls import path
from . import views


urlpatterns = [
    path('', views.patient_list),
    path('<slug:id>/', views.patient_detail),
]
