# Generated by Django 4.1.2 on 2022-10-07 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maestra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maes_nombre', models.CharField(max_length=30)),
                ('maes_valor', models.CharField(max_length=20)),
                ('maes_dependencia', models.CharField(max_length=10)),
                ('maes_tipo_estado', models.CharField(max_length=10)),
            ],
        ),
    ]
