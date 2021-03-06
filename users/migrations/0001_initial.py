# Generated by Django 3.2.9 on 2021-11-22 16:11

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='номер телефона')),
                ('email', models.EmailField(max_length=255, verbose_name='e-mail')),
                ('first_name', models.CharField(max_length=255, verbose_name='имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='фамилие')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='дата последнего входа')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')),
                ('is_staff', models.BooleanField(default=False, verbose_name='персонал')),
                ('is_active', models.BooleanField(default=True, verbose_name='активен')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['-date_joined'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('pub_id', models.CharField(editable=False, max_length=50, unique=True, verbose_name='идентификатор клиента')),
                ('patronymic', models.CharField(max_length=255, verbose_name='отчество')),
                ('status', models.IntegerField(choices=[(None, 'Выберите статус'), (0, 'Неактивен'), (1, 'Активен')], max_length=1, verbose_name='статус')),
                ('status_changed_date', models.DateTimeField(editable=False, verbose_name='дата изменения статуса')),
                ('type', models.IntegerField(choices=[(None, 'Выберите тип'), (1, 'Первичный'), (2, 'Повторный'), (3, 'Внешний'), (4, 'Косвенный')], max_length=1, verbose_name='тип')),
                ('sex', models.IntegerField(choices=[(None, 'Выберите пол'), (1, 'Мужской'), (2, 'Женский'), (3, 'Неизвестно')], max_length=1, verbose_name='пол')),
                ('timezone', timezone_field.fields.TimeZoneField(choices_display='WITH_GMT_OFFSET', default='Europe/Moscow', verbose_name='часовой пояс')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['-date_joined'],
            },
            bases=('users.user',),
        ),
    ]
