from django.db import models

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)                  
    bio = models.TextField(blank=True, null=True)            
    phone_number = models.CharField(max_length=20, blank=True, null=True) 
    birth_date = models.DateField(blank=True, null=True)    
    country = models.CharField(max_length=100, blank=True, null=True)    

    def __str__(self):
        return f"ID:{self.id} | {self.name}"