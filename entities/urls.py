from django.urls import path

from . import views

app_name = 'entities'

urlpatterns = [
    path('departments/', views.DepartmentListAPIView.as_view(), name='departments-list'),
]
