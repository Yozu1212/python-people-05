# Generated by Django 4.1.7 on 2023-04-24 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_nkustnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneMaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.phonemaker')),
            ],
            options={
                'ordering': ['-price'],
            },
        ),
    ]
