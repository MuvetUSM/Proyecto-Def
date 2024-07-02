# Generated by Django 4.2.5 on 2024-07-02 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_rename_nombre_curso_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='cursos',
            fields=[
                ('Numeracion_curso', models.IntegerField(null=True)),
                ('Nombre_curso', models.CharField(choices=[('BA', 'Basico'), ('ME', 'Medio')], max_length=40)),
                ('Codigo_curso', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Paralelo',
            fields=[
                ('codigo_paralelo', models.AutoField(primary_key=True, serialize=False)),
                ('Numero_paralelo', models.IntegerField()),
                ('curso_paralelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.cursos')),
            ],
        ),
    ]