# Generated by Django 4.2.10 on 2024-02-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_name_user_login_remove_user_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='author',
            field=models.CharField(max_length=30),
        ),
    ]