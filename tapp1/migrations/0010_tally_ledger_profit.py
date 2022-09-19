# Generated by Django 4.0.4 on 2022-09-17 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tapp1', '0009_add_voucher3'),
    ]

    operations = [
        migrations.CreateModel(
            name='tally_ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255, null=True)),
                ('under', models.CharField(max_length=255)),
                ('mname', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('bank_details', models.CharField(max_length=20, null=True)),
                ('pan_no', models.CharField(max_length=100, null=True)),
                ('registration_type', models.CharField(max_length=100, null=True)),
                ('gst_uin', models.CharField(max_length=100, null=True)),
                ('set_alter_gstdetails', models.CharField(max_length=100, null=True)),
                ('opening_blnc', models.IntegerField(null=True)),
                ('set_odl', models.CharField(max_length=255, null=True)),
                ('ac_holder_nm', models.CharField(max_length=255, null=True)),
                ('acc_no', models.CharField(max_length=255, null=True)),
                ('ifsc_code', models.CharField(max_length=255, null=True)),
                ('swift_code', models.CharField(max_length=255, null=True)),
                ('bank_name', models.CharField(max_length=255, null=True)),
                ('branch', models.CharField(max_length=255, null=True)),
                ('SA_cheque_bk', models.CharField(max_length=20, null=True)),
                ('Echeque_p', models.CharField(max_length=20, null=True)),
                ('SA_chequeP_con', models.CharField(max_length=20, null=True)),
                ('type_of_ledger', models.CharField(max_length=100, null=True)),
                ('rounding_method', models.CharField(max_length=100, null=True)),
                ('rounding_limit', models.IntegerField(blank=True, default=None, null=True)),
                ('type_duty_tax', models.CharField(max_length=100, null=True)),
                ('tax_type', models.CharField(max_length=100, null=True)),
                ('valuation_type', models.CharField(max_length=100, null=True)),
                ('rate_per_unit', models.IntegerField(blank=True, default=None, null=True)),
                ('percentage_of_calcution', models.CharField(max_length=100, null=True)),
                ('rond_method', models.CharField(max_length=100, null=True)),
                ('rond_limit', models.IntegerField(blank=True, default=None, null=True)),
                ('gst_applicable', models.CharField(max_length=100, null=True)),
                ('setalter_gstdetails', models.CharField(max_length=20, null=True)),
                ('type_of_supply', models.CharField(max_length=100, null=True)),
                ('assessable_value', models.CharField(max_length=100, null=True)),
                ('appropriate_to', models.CharField(max_length=100, null=True)),
                ('method_of_calculation', models.CharField(max_length=100, null=True)),
                ('balance_billbybill', models.CharField(max_length=100, null=True)),
                ('credit_period', models.CharField(max_length=100, null=True)),
                ('creditdays_voucher', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(blank=True, default=0, null=True)),
                ('debit', models.IntegerField(blank=True, default=0, null=True)),
                ('tally_ledger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tapp1.tally_ledger')),
            ],
        ),
    ]