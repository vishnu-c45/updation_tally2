# Generated by Django 4.0.4 on 2022-08-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp1', '0004_payhead_crt'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_payhead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('pay_type', models.CharField(max_length=225)),
                ('income_type', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('affect_net', models.CharField(max_length=225)),
                ('payslip', models.CharField(max_length=225)),
                ('calculation_of_gratuity', models.CharField(max_length=225)),
                ('cal_type', models.CharField(max_length=225)),
                ('calculation_period', models.CharField(max_length=225)),
                ('leave_withpay', models.CharField(max_length=225)),
                ('leave_with_out_pay', models.CharField(max_length=225)),
                ('production_type', models.CharField(max_length=225)),
                ('opening_balance', models.CharField(max_length=225)),
                ('compute', models.CharField(default='Null', max_length=225)),
                ('effective_from', models.CharField(default='NULL', max_length=225)),
                ('amount_greater', models.CharField(default='NULL', max_length=225)),
                ('amount_upto', models.CharField(default='NULL', max_length=225)),
                ('slab_type', models.CharField(default='NULL', max_length=225)),
                ('value', models.CharField(default='NULL', max_length=225)),
                ('Rounding_Method', models.CharField(blank=True, default='Null', max_length=225)),
                ('Round_limit', models.CharField(blank=True, default='Null', max_length=22)),
                ('days_of_months', models.CharField(max_length=225)),
                ('number_of_months_from', models.CharField(max_length=225)),
                ('to', models.CharField(max_length=225)),
                ('calculation_per_year', models.CharField(max_length=225)),
            ],
        ),
    ]