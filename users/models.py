from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField

from .constants import TypeChoices, StatusChoices, SexChoices
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Base user model"""

    phone = PhoneNumberField('номер телефона', unique=True)
    email = models.EmailField('e-mail', max_length=255, unique=True)
    first_name = models.CharField('имя', max_length=255)
    last_name = models.CharField('фамилие', max_length=255)

    last_login = models.DateTimeField('дата последнего входа', auto_now=True)
    date_joined = models.DateTimeField('дата регистрации', auto_now_add=True)

    is_staff = models.BooleanField('персонал', default=False)
    is_active = models.BooleanField('активен', default=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone

    def get_short_name(self):
        return self.first_name

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'


class Customer(User):
    """Model for the customer user"""

    pub_id = models.CharField('идентификатор клиента', unique=True, max_length=50, editable=False)
    patronymic = models.CharField('отчество', max_length=255)
    status = models.IntegerField('статус', choices=StatusChoices.choices)
    status_changed_date = models.DateTimeField('дата изменения статуса', editable=False, null=True)
    type = models.IntegerField('тип', choices=TypeChoices.choices)
    sex = models.IntegerField('пол', choices=SexChoices.choices)
    timezone = TimeZoneField('часовой пояс', default='Europe/Moscow', choices_display='WITH_GMT_OFFSET')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.pub_id = f'{self.id}01'
        return super(Customer, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'клиент'
        verbose_name_plural = 'Клиенты'


class AdditionalPhoneNumber(models.Model):
    phone = PhoneNumberField('дополнительный номер телефона', unique=True)
    customer = models.ForeignKey(Customer, verbose_name='клиент', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'дополнительный номер'
        verbose_name_plural = 'Дополнительные номера'


class AdditionalEmail(models.Model):
    email = models.EmailField('e-mail', max_length=255, unique=True)
    customer = models.ForeignKey(Customer, verbose_name='клиент', on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'дополнительный E-mail'
        verbose_name_plural = 'Дополнительные E-mail'



