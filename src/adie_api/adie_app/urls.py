from django.urls import path
from .views import AdieListView, CompanyListView, OfferListView

urlpatterns = [
    path('', AdieListView.as_view()),
    path('adielist/', AdieListView.as_view()),
    path('companylist/', CompanyListView.as_view()),
    path('offerlist/', OfferListView.as_view()),
]
