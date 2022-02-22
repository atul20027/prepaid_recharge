# Generated by Django 4.0.2 on 2022-02-20 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userrecharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_id', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('operator_id', models.IntegerField()),
                ('recharge_date', models.DateTimeField(auto_now_add=True)),
                ('activation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plans_name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('internet_data', models.CharField(max_length=50)),
                ('call_hours', models.CharField(max_length=50)),
                ('sms_data', models.CharField(max_length=50)),
                ('operator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.operator')),
            ],
        ),
    ]
