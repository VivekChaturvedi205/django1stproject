# Generated by Django 3.2.5 on 2021-09-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_client1_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client1',
            name='Phone',
            field=models.CharField(max_length=250),
        ),
    ]
