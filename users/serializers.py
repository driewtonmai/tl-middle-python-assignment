from rest_framework import serializers

from .models import Customer


class TimezoneField(serializers.Field):
    def to_representation(self, obj):
        if not obj:
            return None

        if isinstance(obj.zone, str):
            return obj.zone


class CustomerSerializer(serializers.ModelSerializer):
    timezone = TimezoneField()
    status = serializers.CharField(source='get_status_display')
    type = serializers.CharField(source='get_type_display')
    sex = serializers.CharField(source='get_sex_display')
    entity = serializers.SlugRelatedField(slug_field='full_name', read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'pub_id', 'phone', 'email', 'first_name', 'last_name',
                  'patronymic', 'status', 'type', 'sex', 'timezone', 'entity')