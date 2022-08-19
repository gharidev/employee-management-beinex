from django import forms

from core.models import Employee

class DateInput(forms.DateInput):
    """Custom date input class to explicitly set the input type to `date`"""
    input_type = 'date'

class EmployeeForm(forms.ModelForm):
    """Employee form for creating & updating an employee."""

    class Meta:
        model = Employee
        fields = ['name', 'code', 'job_title', 'phone', 'email', 'hire_date']
        widgets = {
            'hire_date': DateInput(),
        }

class SalaryForm(forms.ModelForm):
    """Salary form for updating salary details of an employee."""

    name = forms.CharField(disabled=True)
    code = forms.CharField(disabled=True)

    class Meta:
        model = Employee
        fields = ['name', 'code', 'salary']