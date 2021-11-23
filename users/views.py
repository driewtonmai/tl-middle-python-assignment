from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .models import Customer
from .serializers import CustomerSerializer


class CustomerListAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer