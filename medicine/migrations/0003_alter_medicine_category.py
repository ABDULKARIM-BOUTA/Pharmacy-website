# Generated by Django 5.2 on 2025-05-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_alter_medicine_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='category', to='medicine.category'),
        ),
    ]
