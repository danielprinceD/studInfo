# Generated by Django 4.2.4 on 2023-08-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cseStud', '0005_alter_csestud_dob_alter_csestud_fathername_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csestud',
            name='Class',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]