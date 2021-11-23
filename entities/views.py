from django.shortcuts import render
from mptt.templatetags.mptt_tags import cache_tree_children

from rest_framework.generics import ListAPIView

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentListAPIView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        # qs = cache_tree_children(Department.objects.filter(level=0))
        qs = Department.objects.filter(level=0)
        print(qs)
        return qs
