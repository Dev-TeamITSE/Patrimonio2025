# Generated by Django 5.2.2 on 2025-06-06 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0006_noticia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='area',
            field=models.CharField(blank=True, choices=[('Historia', 'Historia'), ('Bellas Artes', 'Bellas Artes'), ('Antropología', 'Antropología'), ('Staff', 'Staff')], max_length=50, null=True),
        ),
    ]
