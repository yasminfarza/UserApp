# Generated by Django 3.1.3 on 2020-11-07 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='person_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address_details', to='accounts.person'),
        ),
    ]