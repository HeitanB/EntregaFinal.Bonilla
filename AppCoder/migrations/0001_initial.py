
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEstudiante', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('programa', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('programa', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Programa', models.CharField(max_length=20)),
                ('codigo', models.CharField(max_length=40)),
            ],
        ),
    ]
