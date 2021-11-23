from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from mptt.models import MPTTModel, TreeForeignKey

from users.constants import ENTITY_CODE, DEPARTMENT_CODE
from users.models import Customer

from .constants import MAX_TREE_DEPTH


class Entity(models.Model):
    pub_id = models.CharField('идентификатор юр. лица', max_length=50, editable=False)
    full_name = models.CharField('полное название', max_length=255)
    short_name = models.CharField('сокращенное название', max_length=50)
    INN = models.CharField('ИНН', max_length=25)
    KPP = models.CharField('КПП', max_length=25)
    created = models.DateTimeField('дата создания', auto_now_add=True)
    updated = models.DateTimeField('дата редактирования', auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-created']
        verbose_name = 'юридическое лицо'
        verbose_name_plural = 'Юридические лица'


@receiver(post_save, sender=Entity)
def create_pub_id_for_entity(sender, instance, created, **kwargs):
    if created:
        Entity.objects.filter(id=instance.id).update(pub_id=f'{instance.id}{ENTITY_CODE}')


class Department(MPTTModel):
    pub_id = models.CharField('идентификатор юр. лица', max_length=50, editable=False)
    name = models.CharField('название', max_length=255)
    entity = models.ForeignKey(Entity, verbose_name='юр. лицо', on_delete=models.PROTECT)
    customers = models.ManyToManyField(Customer, verbose_name='клиенты', through='CustomerDepartmentThrough')
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def clean(self):
        parent_level = self.parent.get_level()
        if parent_level + 1 >= MAX_TREE_DEPTH:
            raise ValidationError({'parent': f'Максимальная глубина дерева {MAX_TREE_DEPTH} была достигнута'})

    class Meta:
        verbose_name = 'департамент'
        verbose_name_plural = 'Департаменты'

    class MPTTMeta:
        order_insertion_by = ['name']


@receiver(post_save, sender=Department)
def create_pub_id_for_department(sender, instance, created, **kwargs):
    if created:
        Department.objects.filter(id=instance.id).update(pub_id=f'{instance.id}{DEPARTMENT_CODE}')


class CustomerDepartmentThrough(models.Model):
    department = models.ForeignKey(Customer, verbose_name='клиент', on_delete=models.CASCADE)
    customer = models.ForeignKey(Department, verbose_name='департамент', on_delete=models.CASCADE)
    date_joined = models.DateTimeField('время добавления клиента', auto_now_add=True)

    def __str__(self):
        return f'{self.customer} {self.department}'

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'дата добавления клиента'
        verbose_name_plural = 'Даты добавления клиентов'
