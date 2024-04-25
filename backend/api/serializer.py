from rest_framework import serializers
from .models import *

class RawPDFSerializer(serializers.ModelSerializer):
    pdf_name = serializers.CharField(source='pdf_file.name', read_only=True)

    class Meta:
        model = RawPDF
        fields = ('pdf_name', 'pdf_file')

class ExtractedTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedText
        fields = ('text_content', 'id')