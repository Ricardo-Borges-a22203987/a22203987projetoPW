# Generated by Django 4.0.6 on 2024-03-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('ano', models.IntegerField(blank=True, choices=[(1, '1º ano'), (2, '2º ano'), (3, '3º ano')], null=True)),
            ],
        ),
    ]