from django.contrib import admin

from .models import Department, Entity, CustomerDepartmentThrough


admin.site.register(CustomerDepartmentThrough)


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
class DepartmentAdmin(admin.ModelAdmin):
    fields = ('pub_id', 'name', 'entity')
    readonly_fields = ('pub_id',)
    list_display = ('pub_id', 'name', 'entity', 'get_count_of_customers')
    inlines = [CustomerDepartmentThroughInline]

    def get_count_of_customers(self, obj):
        return obj.customers.count()

    get_count_of_customers.short_description = 'Количество клиентов'
