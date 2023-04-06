# Generated by Django 4.1.7 on 2023-04-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Giocatore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('soprannome', models.CharField(max_length=50)),
                ('punti_totalizzati', models.IntegerField(default=0)),
                ('partite_giocate', models.IntegerField(default=0)),
            ],
        ),
    ]
