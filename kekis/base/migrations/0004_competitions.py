# Generated by Django 4.2.4 on 2023-09-07 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_timetable_account_projects_group_account_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('kvantum', models.CharField(choices=[('VR', 'Vr'), ('IT', 'It'), ('MEDIA', 'Media'), ('IND-DESIGN', 'Ind-Design'), ('ENERGY', 'Energy'), ('BIO', 'Bio'), ('NEURO', 'Neuro'), ('NANO', 'Nano'), ('HI-TECH', 'Hi-Tech'), ('GEO', 'Geo'), ('AERO', 'Aero'), ('IND-ROBO', 'Ind-Robo')], max_length=10, verbose_name='Квантум')),
                ('description', models.TextField(verbose_name='Описание конкурса')),
                ('contacts', models.CharField(max_length=250, verbose_name='Ссылка на конкурс')),
                ('date', models.DateTimeField(default=None)),
                ('face', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Image_Face_Comp', to='base.image', verbose_name='Обложка на главной странице')),
                ('images', models.ManyToManyField(blank=True, null=True, to='base.image', verbose_name='Дополнительные изображения')),
            ],
        ),
    ]
