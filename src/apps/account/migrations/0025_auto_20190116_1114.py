# Generated by Django 2.1.4 on 2019-01-16 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_auto_20190113_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hired',
            field=models.DateField(default=datetime.date(2019, 1, 16)),
        ),
    ]
