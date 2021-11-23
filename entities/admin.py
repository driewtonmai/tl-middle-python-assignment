from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
from users.models import Customer
from .models import Department, Entity, CustomerDepartmentThrough


@admin.register(CustomerDepartmentThrough)
class CustomerDepartmentThroughAdmin(admin.ModelAdmin):
    fields = ('customer', 'department', 'date_joined')
    readonly_fields = ('date_joined',)
    list_display = ('customer', 'department', 'date_joined')
    search_fields = ('customer', 'department')
    list_filter = ('customer', 'department')


class CustomerDepartmentThroughInline(admin.TabularInline):
    model = CustomerDepartmentThrough
    extra = 1


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    fields = ('pub_id', 'full_name', 'short_name', 'INN', 'KPP', 'created', 'updated')
    readonly_fields = ('pub_id', 'created', 'updated')
    list_display = ('pub_id', 'full_name', 'created')


@admin.register(Department)
class DepartmentAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'name'
    fields = ('pub_id', 'name', 'entity', 'parent')
    readonly_fields = ('pub_id',)
    list_display = ('indented_title', 'pub_id', 'entity', 'get_count_of_customers', 'tree_actions')
    inlines = [CustomerDepartmentThroughInline]
    list_filter = ('name',)
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        print(self)
        qs = Department.objects.add_related_count(
            qs,
            Customer,
            'department',
            'customers_cumulative_count',
            cumulative=True)
        return qs

    def get_count_of_customers(self, instance):
        return instance.customers_cumulative_count

    get_count_of_customers.short_description = 'Количество клиентов'
