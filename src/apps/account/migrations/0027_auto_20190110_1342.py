# Generated by Django 2.1.4 on 2019-01-10 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_requestdayoff_hr_commentary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestdayoff',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='days_off', to=settings.AUTH_USER_MODEL),
        ),
    ]