# Generated by Django 4.0.6 on 2024-04-21 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0003_alter_musica_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='bandas.banda'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='foto_banda',
            field=models.ImageField(blank=True, null=True, upload_to='banda_photos/'),
        ),
        migrations.AlterField(
            model_name='musica',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.album'),
        ),
    ]
