from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializer import *
from rest_framework.response import Response
from .models import *
from .utils import *
from .signals import *

#from rest_framework import viewsets
#Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the home page!")

class RawPDFViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = RawPDF.objects.all()
    serializer_class = RawPDFSerializer
    #this will show us all the data in the database
    #use for recalling all PDFs
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            process_raw_pdf(instance)
            extracted_text_serializer = ExtractedTextSerializer(instance.extracted_text)
            return Response({
                'raw_pdf': serializer.data,
                'extracted_text': extracted_text_serializer.data
            },)
        else:
            return Response(serializer.errors, status=400)
    def retrieve(self, request, pk=None):
        PDF = self.queryset.get(pk=pk)
        serializer = self.serializer_class(PDF)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass
        
    def destroy(self, request, pk=None):
        RawPDF = self.queryset.get(pk=pk)
        RawPDF.delete()
        return Response(status=204)
    
class PDFtextViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = ExtractedText.objects.all()
    serializer_class = ExtractedTextSerializer
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        raw_pdf_instance = queryset.get(pk=pk)
        serializer = self.serializer_class()
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass
        
    def destroy(self, request, pk=None):
        pass