from rest_framework.generics import ListAPIView

from .models import Department, Entity
from .serializers import DepartmentSerializer, EntitySerializer


class DepartmentListAPIView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Department.objects.filter(level=0)


class EntityListAPIView(ListAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer