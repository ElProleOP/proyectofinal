# Generated by Django 4.0.2 on 2022-05-09 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega', '0002_rename_numeroguia_juegomesa_numero_de_guia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libros',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imageneslibros'),
        ),
        migrations.AddField(
            model_name='libros',
            name='sinopsis',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libros',
            name='subido_web',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]