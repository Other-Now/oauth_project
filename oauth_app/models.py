from django.db import models

# Create your models here.

class Employee(models.Model):
    valA=models.DecimalField(max_digits = 5,decimal_places = 2,null=True)
    valB=models.DecimalField(max_digits = 5,decimal_places = 2,null=True)
    valC=models.DecimalField(max_digits = 5,decimal_places = 2,null=True)
    valD=models.DecimalField(max_digits = 5,decimal_places = 2,null=True)
    strA=models.CharField(max_length=100,null=True)

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE