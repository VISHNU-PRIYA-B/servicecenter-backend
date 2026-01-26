from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_repairrequest_status_updaterepairstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
