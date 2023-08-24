from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name',
            'domain',
            'year_founded',
            'industry',
            'size_range',
            'locality',
            'country',
            'linkedin_url',
            'current_employee_estimate',
            'total_employee_estimate',
        ]
