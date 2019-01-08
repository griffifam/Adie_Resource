# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Adie, Company, Offer
from .serializers import AdieSerializer, CompanySerializer, OfferSerializer

class AdieListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Adie.objects.all()
    serializer_class = AdieSerializer

class CompanyListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class OfferListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
