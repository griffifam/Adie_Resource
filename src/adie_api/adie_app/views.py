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

class AdieCreateView(generics.CreateAPIView):
    """
    Provides a post method handler.
    """
    lookup_field = 'pk'
    serializer_class = AdieSerializer

    def get_queryset(self):
        return Adie.Objects.all()

class CompanyListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyCreateView(generics.CreateAPIView):
    """
    Provides a post method handler.
    """
    lookup_field = 'pk'
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.Objects.all()

class OfferListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferCreateView(generics.CreateAPIView):
    """
    Provides a post method handler.
    """
    lookup_field = 'pk'
    serializer_class = OfferSerializer

    def get_queryset(self):
        return Offer.Objects.all()
