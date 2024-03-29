# Generated by Django 3.1.2 on 2020-11-05 14:19

import PeliSeries.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categ', models.CharField(max_length=200, unique=True, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, null=True)),
                ('fecha', models.DateField(default=django.utils.timezone.now, null=True)),
                ('correo', models.EmailField(max_length=254, null=True)),
                ('motivo', models.CharField(max_length=30, null=True)),
                ('consulta', models.TextField(max_length=200, null=True)),
                ('fecharespuesta', models.DateField(null=True)),
                ('respuesta', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Género')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('contraseña', models.CharField(max_length=8)),
                ('img_usuario', models.ImageField(upload_to=PeliSeries.models.img_user)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Admim')),
            ],
        ),
        migrations.CreateModel(
            name='Peliserie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(blank=True, max_length=200, null=True, verbose_name='Autor/a')),
                ('reparto', models.CharField(blank=True, max_length=200, null=True)),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descripcion', models.CharField(max_length=1500, verbose_name='Descripción')),
                ('genero', models.CharField(max_length=200, verbose_name='Género')),
                ('year_estreno', models.PositiveSmallIntegerField(verbose_name='Año de Estreno')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Publicación')),
                ('caratula', models.ImageField(blank=True, null=True, upload_to=PeliSeries.models.ruta_imagen)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Admim')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PeliSeries.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(blank=True, max_length=1500, null=True, verbose_name='enunciado')),
                ('img_carousel', models.ImageField(blank=True, null=True, upload_to=PeliSeries.models.ruta_img_carousel, verbose_name='imagen')),
                ('fecha_public', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Publicación')),
                ('visible', models.BooleanField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PeliSeries.categoria')),
                ('peliserie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PeliSeries.peliserie')),
            ],
        ),
    ]
