# Generated by Django 4.0.4 on 2022-04-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CALC', '0004_alter_operands_operator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operands',
            name='operator',
            field=models.CharField(default=0, max_length=1),
        ),
    ]