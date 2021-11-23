from rest_framework import serializers

from users.serializers import CustomerSerializer
from .models import Department, Entity


class DepartmentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'pub_id', 'name', 'entity', 'customers', 'parent', 'children')

    def get_children(self, obj):
        return DepartmentSerializer(obj.get_children(), many=True).data


class EntitySerializer(serializers.ModelSerializer):
    department_set = DepartmentSerializer(many=True, read_only=True)
    customer_set = CustomerSerializer(many=True, read_only=True)

    class Meta:
        model = Entity
        fields = ('id', 'pub_id', 'full_name', 'short_name', 'INN', 'KPP', 'customer_set', 'department_set')