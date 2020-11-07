# Generated by Django 3.1.3 on 2020-11-07 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201107_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='person_id',
            new_name='person',
        ),
        migrations.AlterField(
            model_name='person',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.person', verbose_name='Parent'),
        ),
    ]
