from django.db import models

# Create your models here.

class Category(models.Model):
    
    category_name = models.CharField(max_length=225)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    updated_date = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.category_name
    
    
class Employee(models.Model):
    
    employee_name = models.CharField(max_length=225)
    
    Category_object = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    place = models.CharField(max_length=225)
    
    mobile_number = models.CharField(max_length=225)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    updated_date = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self) :
        return self.employee_name
    
    
    