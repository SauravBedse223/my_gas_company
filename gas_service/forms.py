from django import forms

class ServiceRequestForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    request = forms.CharField(widget=forms.Textarea)  # Ensure this field is present
