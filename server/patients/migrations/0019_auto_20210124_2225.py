# Generated by Django 3.1.1 on 2021-01-24 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20201120_1722'),
        ('patients', '0018_patient_warning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='resources.resource'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='warning',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
