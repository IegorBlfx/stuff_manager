# Generated by Django 2.1.4 on 2019-01-03 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20190103_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='salary',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Position'),
        ),
    ]
