# Generated by Django 2.1.4 on 2019-01-04 12:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_remove_user_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=100, null=True)),
                ('tax', models.PositiveSmallIntegerField(default=40)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='hired',
            field=models.DateField(default=datetime.date(2019, 1, 4)),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Country'),
        ),
    ]
