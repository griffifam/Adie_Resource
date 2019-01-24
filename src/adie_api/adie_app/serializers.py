from rest_framework import serializers
from .models import Adie, Company, Offer


class AdieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adie
        fields = [
        "age",
        "gender",
        "location_city",
        "location_state",
        "orientation",
        "race",
        "transplant"
        ]
class AdieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adie
        fields = [
        "age",
        "gender",
        "location_city",
        "location_state",
        "orientation",
        "race",
        "transplant"
        ]

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("adies_present", "industry", "location_city", "location_state", "org_size", "company_size", "level_of_microaggressions")

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ("base_amount", "health_insurance", "relocation_package", "signing_bonus", "adie_id", "company_id", "retirement", "vacation_days", "hire_type", "negotiations", "stocks")

# converts to JSON
# Validates for data passed
