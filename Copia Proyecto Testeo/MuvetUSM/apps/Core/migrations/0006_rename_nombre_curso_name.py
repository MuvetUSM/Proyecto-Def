# Generated by Django 5.0.4 on 2024-07-01 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_rename_name_curso_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='nombre',
            new_name='name',
        ),
    ]