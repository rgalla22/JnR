import uuid
from django.db import models

class RawPDF(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pdf_file = models.FileField(upload_to='pdf/')
    uploaded_date = models.DateField(auto_now_add=True)
    pdf_name = models.CharField(max_length=255, blank=False, null=True)

    def __str__(self):
        return str(self.id)

class ExtractedText(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    raw_pdf = models.OneToOneField(RawPDF, on_delete=models.CASCADE, related_name='extracted_text')
    text_content = models.TextField(default="", blank=False, null=True)


def __str__(self):
        return f"ExtractedText for {self.raw_pdf}"
