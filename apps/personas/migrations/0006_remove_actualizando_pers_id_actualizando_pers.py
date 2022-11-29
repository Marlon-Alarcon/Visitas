# Generated by Django 4.1.2 on 2022-11-20 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_actualizando_pers_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actualizando',
            name='pers_id',
        ),
        migrations.AddField(
            model_name='actualizando',
            name='pers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pers', to='personas.persona'),
        ),
    ]