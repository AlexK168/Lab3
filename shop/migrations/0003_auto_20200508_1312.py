# Generated by Django 3.0.6 on 2020-05-08 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_manager_outlet_tag_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='outlet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Outlet'),
        ),
        migrations.AddField(
            model_name='product',
            name='outlet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Outlet'),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Vendor'),
        ),
    ]
