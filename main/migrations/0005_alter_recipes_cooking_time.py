# Generated by Django 4.2.10 on 2024-02-12 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_user_alter_recipes_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='cooking_time',
            field=models.IntegerField(),
        ),
    ]