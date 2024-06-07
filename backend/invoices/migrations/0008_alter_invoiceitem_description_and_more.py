# Generated by Django 4.2.13 on 2024-06-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0007_alter_invoice_options_invoice_date_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='ref_job_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
