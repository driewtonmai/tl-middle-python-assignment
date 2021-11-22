from django.contrib import admin
from django.contrib.auth.models import Group

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import Customer, User, SocialNetwork, Facebook, Vkontakte, AdditionalEmail, AdditionalPhoneNumber


admin.site.unregister(Group)
admin.site.register(AdditionalEmail)
admin.site.register(AdditionalPhoneNumber)


class AdditionalEmailInline(NestedStackedInline):
    model = AdditionalEmail
    extra = 1


class AdditionalPhoneNumberInline(NestedStackedInline):
    model = AdditionalPhoneNumber
    extra = 1


class VkontakteInline(NestedStackedInline):
    model = Vkontakte
    extra = 1
    fk_name = 'social_network'


class FacebookInline(NestedStackedInline):
    model = Facebook
    extra = 1
    fk_name = 'social_network'


class SocialNetworkInline(NestedStackedInline):
    model = SocialNetwork
    fk_name = 'customer'
    inlines = [FacebookInline, VkontakteInline]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'
    fields = ('phone', 'email', 'first_name', 'last_name',
              'last_login', 'date_joined', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    readonly_fields = ('last_login', 'date_joined')
    list_display = ('phone', 'last_name', 'first_name', 'email')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_staff=True)


@admin.register(Customer)
class CustomerAdmin(NestedModelAdmin):
    date_hierarchy = 'date_joined'
    fields = ('pub_id', 'phone', 'email', 'first_name', 'last_name',
              'patronymic', 'status', 'status_changed_date', 'type', 'sex',
              'timezone', 'last_login', 'date_joined', 'is_active', 'is_staff')
    readonly_fields = ('pub_id', 'last_login', 'date_joined', 'status_changed_date')
    inlines = [AdditionalEmailInline, AdditionalPhoneNumberInline, SocialNetworkInline]
    list_display = ('pub_id', 'last_name', 'first_name', 'patronymic', 'phone', 'email')


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    inlines = [FacebookInline, VkontakteInline]
