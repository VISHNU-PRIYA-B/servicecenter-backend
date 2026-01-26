from django.db import migrations, models

def populate_invoice_numbers(apps, schema_editor):
    Invoice = apps.get_model('service', 'Invoice')
    for inv in Invoice.objects.all():
        inv.invoice_number = f"INV-{str(inv.id).zfill(5)}"
        inv.save()

class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_invoice_invoice_number'),
    ]

    operations = [
        migrations.RunPython(populate_invoice_numbers),

        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
