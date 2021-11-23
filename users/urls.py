from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.CustomerListAPIView.as_view(), name='customers-list'),
]
