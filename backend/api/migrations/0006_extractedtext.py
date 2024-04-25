# Generated by Django 5.0.4 on 2024-04-24 07:06

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rawpdf_pdf_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractedText',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text_content', models.TextField(blank=True, null=True)),
                ('raw_pdf', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extracted_text', to='api.rawpdf')),
            ],
        ),
    ]