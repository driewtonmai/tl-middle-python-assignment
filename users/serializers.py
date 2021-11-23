from rest_framework import serializers

from .models import Customer, AdditionalPhoneNumber, AdditionalEmail, SocialNetwork, Vkontakte, Facebook


class TimezoneField(serializers.Field):
    def to_representation(self, obj):
        if not obj:
            return None

        if isinstance(obj.zone, str):
            return obj.zone


class AdditionalPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalPhoneNumber
        fields = ('phone',)


class AdditionalEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalEmail
        fields = ('email',)


class VkontakteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vkontakte
        fields = ('url',)


class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facebook
        fields = ('url',)


class SocialNetworkSerializer(serializers.ModelSerializer):
    vkontakte_set = VkontakteSerializer(many=True, read_only=True)
    facebook_set = FacebookSerializer(many=True, read_only=True)

    class Meta:
        model = SocialNetwork
        fields = ('instagram', 'telegram', 'whatsapp', 'viber', 'vkontakte_set', 'facebook_set')


class CustomerSerializer(serializers.ModelSerializer):
    timezone = TimezoneField()
    status = serializers.CharField(source='get_status_display')
    type = serializers.CharField(source='get_type_display')
    sex = serializers.CharField(source='get_sex_display')
    entity = serializers.SlugRelatedField(slug_field='full_name', read_only=True)
    additionalphonenumber_set = AdditionalPhoneNumberSerializer(read_only=True, many=True)
    additionalemail_set = AdditionalEmailSerializer(read_only=True, many=True)
    socialnetwork = SocialNetworkSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'pub_id', 'phone', 'email', 'first_name', 'last_name',
                  'patronymic', 'status', 'type', 'sex', 'timezone', 'entity', 'additionalphonenumber_set',
                  'additionalemail_set', 'socialnetwork')
        depth = 1