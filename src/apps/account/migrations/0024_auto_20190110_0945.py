# Generated by Django 2.1.4 on 2019-01-10 09:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestDayOff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('confirmed', models.CharField(blank=True, choices=[('A', 'Accept'), ('D', 'Declaine')], max_length=1, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='hired',
            field=models.DateField(default=datetime.date(2019, 1, 10)),
        ),
        migrations.AddField(
            model_name='requestdayoff',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]