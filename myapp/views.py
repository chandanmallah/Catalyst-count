
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .serializers import CompanySerializer
from .models import Company
import pandas as pd
from django import forms
import csv
# from accounts.models import MyUser
from ninja import NinjaAPI
# from ninja.security import APIKeyHeader
# from knox.models import AuthToken

myapp_api = NinjaAPI(version='2.0.0')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dataupload')  
        else:
            
            return render(request, 'myapp/login.html', {'error_message': 'Invalid credentials. Please try again.'})

    return render(request, 'myapp/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label="Choose a CSV file", widget=forms.FileInput(attrs={'accept': '.csv'}), required=False)

@login_required
def data_upload_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csvFile']
            try:
                decoded_file = csv_file.read().decode('utf-8')
                csv_reader = csv.DictReader(decoded_file.splitlines())
                for row in csv_reader:
                    try:
                        Company.objects.create(
                            name=row['name'],
                            domain=row['domain'],
                            year_founded=int(row['year founded']) if row.get('year founded') else None,
                            industry=row['industry'] if row.get('industry') else None,
                            size_range=row['size range'] if row.get('size range') else None,
                            locality=row['locality'] if row.get('locality') else None,
                            country=row['country'] if row.get('country') else None,
                            linkedin_url=row['linkedin url'] if row.get('linkedin url') else None,
                            current_employee_estimate=int(row['current employee estimate']) if row.get('current employee estimate') else None,
                            total_employee_estimate=int(row['total employee estimate']) if row.get('total employee estimate') else None,
                        )
                    except (ValueError, TypeError):
                        # Conversion error 
                        Company.objects.create(
                            name=None,
                            domain=None,
                            year_founded=None,
                            industry=None,
                            size_range=None,
                            locality=None,
                            country=None,
                            linkedin_url=None,
                            current_employee_estimate=None,
                            total_employee_estimate=None,
                        )
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
    else:
        form = CSVUploadForm()
    return render(request, 'myapp/dataupload.html', {'form': form})



@login_required
@api_view(['GET', 'POST'])
def query_builder_view(request):
    name_filter = request.data.get('name', '')
    year_founded_filter = request.data.get('year_founded', '')
    industry_filter = request.data.get('industry', '')
    country_filter = request.data.get('country', '')

    filtered_companies = Company.objects.filter(
        name__icontains=name_filter,
        year_founded__icontains=year_founded_filter,
        industry__icontains=industry_filter,
        country__icontains=country_filter,
    )

    # print(filtered_companies)
    serializer = CompanySerializer(filtered_companies, many=True)

    count = filtered_companies.count()
    # print(count)

    # rendering the template
    return render(request, 'myapp/querybuilder.html', {'count': count, 'data': serializer.data})

@login_required
def query_builder_template_view(request):
    return render(request, 'myapp/querybuilder.html')

@login_required
def users_view(request):
    users = User.objects.all()
    return render(request, 'myapp/users.html', {'users': users})
