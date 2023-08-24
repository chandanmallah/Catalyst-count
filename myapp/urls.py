# myapp/urls.py

from django.urls import path,include
from . import views
from rest_framework import routers
# from myapp.views import CompanyViewSet

router = routers.DefaultRouter()
from myapp.views import *
# router.register(r'companies', CompanyViewSet)

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dataupload/', views.data_upload_view, name='dataupload'),
    path('querybuilder/', views.query_builder_view, name='querybuilder'),
    path('users/', views.users_view, name='users'),
    path('logout/', views.logout_view, name='logout'),
    # path('querybuilder/template/', query_builder_template_view, name='querybuilder'), # Updated name
    path('querybuilder/template', query_builder_template_view, name='querybuilder_template'),
    # path("", myapp_api.urls, name="dataupload"),
]


