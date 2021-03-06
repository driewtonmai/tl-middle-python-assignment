# Generated by Django 3.2.9 on 2021-11-23 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
        ('users', '0007_alter_customer_pub_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='entities.entity', verbose_name='юр. лицо'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Мужской'), (2, 'Женский'), (3, 'Неизвестно')], default=3, verbose_name='пол'),
        ),
    ]
