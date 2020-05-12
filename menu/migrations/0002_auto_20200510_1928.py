# Generated by Django 3.0.5 on 2020-05-10 19:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_checkin'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kot',
            fields=[
                ('kot_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(default=datetime.date.today)),
                ('order_time', models.TimeField(auto_now_add=True)),
                ('status', models.CharField(default='Waiting', max_length=15)),
                ('amount', models.FloatField()),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.Members')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(default=datetime.date.today)),
                ('order_time', models.TimeField(auto_now_add=True)),
                ('amount', models.FloatField(default=0)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.Members')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.Staff')),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.Table')),
            ],
        ),
        migrations.CreateModel(
            name='KotItem',
            fields=[
                ('kotitem_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(default='Waiting', max_length=15)),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.Dish')),
                ('kot_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='menu.Kot')),
            ],
        ),
        migrations.AddField(
            model_name='kot',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.Order'),
        ),
        migrations.AddField(
            model_name='kot',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.Staff'),
        ),
        migrations.AddField(
            model_name='kot',
            name='table_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.Table'),
        ),
    ]
