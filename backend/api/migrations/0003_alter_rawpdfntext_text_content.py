# Generated by Django 5.0.4 on 2024-04-24 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rawpdfntext_delete_rawpdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawpdfntext',
            name='text_content',
            field=models.TextField(auto_created=True, null=True),
        ),
    ]
