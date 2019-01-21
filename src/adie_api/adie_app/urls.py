from django.urls import path
from .views import AdieListView, AdieCreateView, CompanyListView, CompanyCreateView, OfferListView, OfferCreateView

urlpatterns = [
    path('', AdieListView.as_view()),
    path('adielist/', AdieListView.as_view()),
    path('adielist/new', AdieCreateView.as_view()),
    path('companylist/', CompanyListView.as_view()),
    path('companylist/new', CompanyCreateView.as_view()),
    path('offerlist/', OfferListView.as_view()),
    path('offerlist/new', OfferCreateView.as_view()),
]
