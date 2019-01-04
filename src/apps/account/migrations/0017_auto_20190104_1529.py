# Generated by Django 2.1.4 on 2019-01-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20190104_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='salary',
            field=models.CharField(default=3200, max_length=10, null=True),
        ),
    ]