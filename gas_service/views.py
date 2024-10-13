from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ServiceRequestForm
from .models import ServiceRequest  # Assuming you have a model for service requests
from django.contrib import messages


def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            request_text = form.cleaned_data['request_text']  # This line accesses the form data correctly
            
            # Save the data to the database
            service_request = ServiceRequest(name=name, email=email, request_text=request_text)
            service_request.save()  # Save the request to the database
            
            # Add a success message
            messages.success(request, "Your request has been submitted successfully!")
            return redirect('request_list')  # Redirect to the request list view after submission
        else:
            messages.error(request, "There were errors in your form. Please correct them.")
    else:
        form = ServiceRequestForm()

    return render(request, 'gas_service/submit_request.html', {'form': form})


def request_list(request):
    requests = ServiceRequest.objects.all()  # Get all service requests
    return render(request, 'gas_service/request_list.html', {'requests': requests})
