# Generated by Django 3.2.9 on 2021-11-23 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0007_alter_customer_pub_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDepartmentThrough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='время добавления клиента')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_id', models.CharField(editable=False, max_length=50, verbose_name='идентификатор юр. лица')),
                ('full_name', models.CharField(max_length=255, verbose_name='полное название')),
                ('short_name', models.CharField(max_length=50, verbose_name='сокращенное название')),
                ('INN', models.CharField(max_length=25, verbose_name='ИНН')),
                ('KPP', models.CharField(max_length=25, verbose_name='КПП')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='дата редактирования')),
            ],
            options={
                'verbose_name': 'юридическое лицо',
                'verbose_name_plural': 'Юридические лица',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_id', models.CharField(editable=False, max_length=50, verbose_name='идентификатор юр. лица')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('customers', models.ManyToManyField(through='entities.CustomerDepartmentThrough', to='users.Customer', verbose_name='клиенты')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entities.entity', verbose_name='юр. лицо')),
            ],
            options={
                'verbose_name': 'департамент',
                'verbose_name_plural': 'Департаменты',
            },
        ),
        migrations.AddField(
            model_name='customerdepartmentthrough',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.department', verbose_name='департамент'),
        ),
        migrations.AddField(
            model_name='customerdepartmentthrough',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer', verbose_name='клиент'),
        ),
    ]
