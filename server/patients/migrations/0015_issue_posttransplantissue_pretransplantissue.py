# Generated by Django 3.1.1 on 2020-11-17 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0014_auto_20201101_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('order', models.PositiveIntegerField()),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PretransplantIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='patients.issue')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='patients.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostTransplantIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='patients.issue')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='patients.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
