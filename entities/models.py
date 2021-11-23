from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.constants import ENTITY_CODE, DEPARTMENT_CODE
from users.models import Customer


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


class Department(models.Model):
    pub_id = models.CharField('идентификатор юр. лица', max_length=50, editable=False)
    name = models.CharField('название', max_length=255)
    entity = models.ForeignKey(Entity, verbose_name='юр. лицо', on_delete=models.PROTECT)
    customers = models.ManyToManyField(Customer, verbose_name='клиенты', through='CustomerDepartmentThrough')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'департамент'
        verbose_name_plural = 'Департаменты'


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
