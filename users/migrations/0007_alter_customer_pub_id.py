# Generated by Django 3.2.9 on 2021-11-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customer_status_changed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pub_id',
            field=models.CharField(editable=False, max_length=50, verbose_name='идентификатор клиента'),
        ),
    ]