from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    domain = models.CharField(max_length=255,null=True, blank=True)
    year_founded = models.FloatField(null=True, blank=True)  # Changed to FloatField
    industry = models.CharField(max_length=255, null=True, blank=True)
    size_range = models.CharField(max_length=255, null=True, blank=True)
    locality = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    current_employee_estimate = models.FloatField(null=True, blank=True)  # Changed to FloatField
    total_employee_estimate = models.FloatField(null=True, blank=True)  # Changed to FloatField
    
    def __str__(self):
        return self.name

