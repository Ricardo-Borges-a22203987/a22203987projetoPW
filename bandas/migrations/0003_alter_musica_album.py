# Generated by Django 4.0.6 on 2024-03-18 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_musica_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bandas.album'),
        ),
    ]