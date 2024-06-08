from django import forms
from myapp.models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        
        model = Employee
        
        fields = "__all__"
        
        read_only_fields = ["id","created_date", "updated_date", "is_active"]