# Generated by Django 4.0.1 on 2022-01-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('web', models.URLField(max_length=500)),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
