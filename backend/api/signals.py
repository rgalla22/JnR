from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpRequest
from .models import RawPDF, ExtractedText
from .utils import process_raw_pdf  # Importing directly from the utils module

@receiver(post_save, sender=RawPDF)
def process_new_pdf(sender, instance, created, **kwargs):
    if created:
        # Check if the request is a POST request to /api/RawPDF/
        if isinstance(instance._state.db, HttpRequest) and instance._state.db.method == "POST" and instance._state.db.path == "/api/RawPDF/":
            try:
                # Process the newly created RawPDF instance
                process_raw_pdf(instance)
                # Create associated ExtractedText instance
                ExtractedText.objects.create(raw_pdf=instance)
            except Exception as e:
                # Handle any exceptions gracefully
                print(f"Error processing RawPDF: {e}")
