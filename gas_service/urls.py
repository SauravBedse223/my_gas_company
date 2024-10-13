from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_request, name='home'),  # Redirect to the submit_request view
    path('submit/', views.submit_request, name='submit_request'),
    path('requests/', views.request_list, name='request_list'),
   
]
