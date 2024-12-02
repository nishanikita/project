from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('employee_list')
    else:
        form = AuthenticationForm()
    return render(request, 'employee_register/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Employee List View
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_register/employee_list.html', {'employees': employees})

# Create Employee View
@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'employee successfully added!')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_register/employee_form.html', {'form': form})

# Update Employee View
@login_required
def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request,'employee successfully updated!')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_register/employee_form.html', {'form': form})

# Delete Employee View
@login_required
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request,'employee successfully deleted!')
        return redirect('employee_list')
    return render(request, 'employee_register/employee_delete.html', {'employee': employee})
