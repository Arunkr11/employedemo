from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Employee,Category
from myapp.forms import EmployeeForm

# Create your views here.

class EmployeeListView(View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        cator=Category.objects.all()
        cat = request.GET.get("category")
        print(cat)
        if cat:
            qs = qs.filter(Category_object__category_name = cat)
            
        return render(request,"employeeslist.html",{'data':qs,"cat":cator})
    
class EmployeeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = EmployeeForm()
        return render(request,"employeescreate.html",{'form':form})
    
    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("employeeslist")
        return render(request,"employeescreate.html",{'form':form})
    
class EmployeeDetailsView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = Employee.objects.get(id=id)
        return render(request,"employeesdetails.html",{"data":qs})
    
class EmployeeupdateView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        e_obj = Employee.objects.get(id=id)
        form = EmployeeForm(instance=e_obj)
        return render(request,"employeesupdate.html",{'form':form})
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        e_obj = Employee.objects.get(id=id)
        form = EmployeeForm(request.POST,instance=e_obj)
        if form.is_valid():
            form.save()
            return redirect("employeeslist")
        return render(request,"employeesupdate.html",{'form':form})
    
class EmployeeDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = Employee.objects.get(id=id).delete()
        return redirect("employeeslist")
    

    
