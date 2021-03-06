# Generated by Django 2.1.4 on 2019-01-06 09:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20190104_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=None, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='position',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=3, default=3200, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='account.City'),
        ),
        migrations.AlterField(
            model_name='user',
            name='hired',
            field=models.DateField(default=datetime.date(2019, 1, 6)),
        ),
    ]
