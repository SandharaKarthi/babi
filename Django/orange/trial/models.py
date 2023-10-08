from django.db import models

# Create your models here.

class employee_details(models.Model):
    Emp_id = models.IntegerField(primary_key=True)
    Emp_name = models.CharField(max_length=50)
    Emp_DOB = models.DateField()
    

 
        
