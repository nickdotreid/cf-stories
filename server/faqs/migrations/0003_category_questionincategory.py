# Generated by Django 3.1.1 on 2021-01-24 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0002_answer_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('order', models.PositiveIntegerField()),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionInCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='faqs.category')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='faqs.frequentlyaskedquestion')),
            ],
        ),
    ]
