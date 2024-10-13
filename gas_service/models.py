from django.db import models

class ServiceRequest(models.Model):
    # Field to store the name of the person submitting the request
    name = models.CharField(max_length=100)
    
    # Field to store the email address of the person
    email = models.EmailField()
    
    # Field to store the text of the request
    request_text = models.TextField()

    def __str__(self):
        # String representation of the model instance
        return f"Request from {self.name} ({self.email})"
