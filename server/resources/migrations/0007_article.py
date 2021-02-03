# Generated by Django 3.1.1 on 2021-02-03 02:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20201120_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('published', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField()),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('content', ckeditor.fields.RichTextField(null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='resources.article')),
            ],
        ),
    ]
