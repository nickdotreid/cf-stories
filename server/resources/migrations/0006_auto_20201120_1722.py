# Generated by Django 3.1.1 on 2020-11-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_remove_definition_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definition',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='definition',
            name='name',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='definition',
            name='slug',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='resource',
            name='slug',
            field=models.CharField(max_length=160, null=True),
        ),
    ]
