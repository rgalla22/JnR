# Generated by Django 5.0.4 on 2024-04-22 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_date', models.DateField(auto_created=True)),
                ('pdf_name', models.CharField(max_length=200, unique=True)),
                ('pdf_file', models.FileField(upload_to='pdf/')),
            ],
        ),
    ]
