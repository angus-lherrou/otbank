# Generated by Django 2.2.7 on 2019-11-07 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otbank', '0002_auto_20191107_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definition',
            name='constraint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otbank.Constraint'),
        ),
    ]