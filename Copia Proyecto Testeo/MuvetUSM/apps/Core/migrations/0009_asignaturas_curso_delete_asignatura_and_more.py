# Generated by Django 4.2.5 on 2024-07-10 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_rename_curso_asignatura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('codigo_asignatura', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_Asignatura', models.CharField(default=None, max_length=50)),
                ('semestre', models.IntegerField(choices=[(1, '1 semestre'), (2, '2 semestre')])),
                ('Asignatura_paralelo', models.ManyToManyField(to='Core.paralelo')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('grado', models.CharField(default=None, max_length=50)),
                ('nivel_educativo', models.CharField(choices=[('Basico', 'Basico'), ('Medio', 'Medio')], max_length=40)),
                ('Codigo_curso', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Asignatura',
        ),
        migrations.AddField(
            model_name='asignaturas',
            name='curso_asociado',
            field=models.ManyToManyField(to='Core.curso'),
        ),
        migrations.AlterField(
            model_name='paralelo',
            name='curso_paralelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.curso'),
        ),
        migrations.DeleteModel(
            name='cursos',
        ),
    ]
