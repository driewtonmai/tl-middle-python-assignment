from rest_framework import serializers

from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'pub_id', 'name', 'entity', 'customers', 'parent', 'children')

    def get_children(self, obj):
        return DepartmentSerializer(obj.get_children(), many=True).data