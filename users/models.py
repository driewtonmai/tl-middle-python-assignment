from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.signals import pre_save, pre_init, post_init, post_save
from django.dispatch import receiver
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

    is_staff = models.BooleanField('сотрудник', default=False)
    is_active = models.BooleanField('активен', default=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.phone)

    def get_short_name(self):
        return self.first_name

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'сотрудник'
        verbose_name_plural = 'Сотрудники'


class Customer(User):
    """Model for the customer user"""

    pub_id = models.CharField('идентификатор клиента', max_length=50, editable=False)
    patronymic = models.CharField('отчество', max_length=255)
    status = models.IntegerField('статус', choices=StatusChoices.choices)
    status_changed_date = models.DateTimeField('дата изменения статуса', editable=False, default=timezone.now)
    type = models.IntegerField('тип', choices=TypeChoices.choices)
    sex = models.IntegerField('пол', choices=SexChoices.choices, default=SexChoices.UNKNOWN)
    timezone = TimeZoneField('часовой пояс', default='Europe/Moscow', choices_display='WITH_GMT_OFFSET')

    def __str__(self):
        return self.pub_id

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def save(self, *args, **kwargs):
        if self.id:
            previous = Customer.objects.only('status').get(id=self.id)
            if previous.status != self.status:
                self.status_changed_date = timezone.now()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'клиент'
        verbose_name_plural = 'Клиенты'


@receiver(post_save, sender=Customer)
def create_pub_id(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.filter(id=instance.id).update(pub_id=f'{instance.id}01')


class AdditionalPhoneNumber(models.Model):
    phone = PhoneNumberField('дополнительный номер телефона', unique=True)
    customer = models.ForeignKey(Customer, verbose_name='клиент', on_delete=models.CASCADE)

    def __str__(self):
        return f'Дополнительные номера пользователя {self.customer.get_full_name()}'

    class Meta:
        verbose_name = 'дополнительный номер'
        verbose_name_plural = 'Дополнительные номера'


class AdditionalEmail(models.Model):
    email = models.EmailField('e-mail', max_length=255, unique=True)
    customer = models.ForeignKey(Customer, verbose_name='клиент', on_delete=models.CASCADE)

    def __str__(self):
        return f'Дополнительные E-mail пользователя {self.customer.get_full_name()}'

    class Meta:
        verbose_name = 'дополнительный E-mail'
        verbose_name_plural = 'Дополнительные E-mail'


class SocialNetwork(models.Model):
    customer = models.OneToOneField(Customer, verbose_name='клиент', on_delete=models.CASCADE)
    instagram = models.URLField('instagram', max_length=255, blank=True, null=True)
    telegram = models.CharField('telegram', max_length=25, blank=True, null=True)
    whatsapp = models.CharField('whatsApp', max_length=25, blank=True, null=True)
    viber = models.CharField('viber', max_length=25, blank=True, null=True)

    def __str__(self):
        return f'Социальные сети пользователя {self.customer.get_full_name()}'

    class Meta:
        verbose_name = 'социальная сеть'
        verbose_name_plural = 'Социальные сети'


class Vkontakte(models.Model):
    social_network = models.ForeignKey(SocialNetwork, verbose_name='социальная сеть', on_delete=models.CASCADE)
    url = models.URLField('ссылка', max_length=255)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'вконтакте'
        verbose_name_plural = 'Вконтакте'


class Facebook(models.Model):
    social_network = models.ForeignKey(SocialNetwork, verbose_name='социальная сеть', on_delete=models.CASCADE)
    url = models.URLField('ссылка', max_length=255)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'facebook'
        verbose_name_plural = 'Facebook'
