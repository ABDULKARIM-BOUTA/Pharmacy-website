# Generated by Django 5.2 on 2025-05-02 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturers', '0001_initial'),
        ('medicine', '0008_alter_medicine_category_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacturers.manufacturer'),
        ),
        migrations.DeleteModel(
            name='Manufacturer',
        ),
    ]
