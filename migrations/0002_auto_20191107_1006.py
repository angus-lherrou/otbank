# Generated by Django 2.2.7 on 2019-11-07 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otbank', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constraint',
            old_name='constraint_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='constraint',
            name='subfield',
        ),
        migrations.AlterField(
            model_name='definition',
            name='constraint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otbank.Constraint', to_field='name'),
        ),
        migrations.DeleteModel(
            name='Subfield',
        ),
    ]