from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('RawPDF', RawPDFViewset, basename="RawPDF")
router.register('PDFtext', PDFtextViewset, basename="PDFtext")
urlpatterns = router.urls
#urlpatterns = [
#    path('', home, name='home'),
#]
