from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from core.forms import EmployeeForm, SalaryForm
from core.models import Employee

class EmployeeListView(LoginRequiredMixin, ListView):
    """Home view for listing the employees with pagination."""
    template_name = 'core/employee-list.html'
    model = Employee
    paginate_by = 10
    context_object_name = 'employees'

class AddEmployeeView(LoginRequiredMixin, CreateView):
    """View for creating an employee."""
    form_class = EmployeeForm
    extra_context = {'title': 'Add Employee'}
    template_name = 'core/form.html'

    def get_success_url(self):
        return reverse('core:edit-salary', kwargs={'pk': self.object.pk})

class EditSalaryView(LoginRequiredMixin, UpdateView):
    """View for updating salary information of an employee."""
    form_class = SalaryForm
    template_name = 'core/form.html'
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = 'Add Salary' if not self.get_object().salary else 'Edit Salary'
        context.update({'title': title})
        return context
    
    def get_success_url(self):
        return reverse('core:employee-detail', kwargs={'pk':self.object.pk})


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    """View for deatiled description of an employee."""
    model = Employee
    context_object_name = 'employee'
    template_name = 'core/employee-detail.html'

class EditEmployeeView(LoginRequiredMixin, UpdateView):
    """View for editing an employee."""
    model = Employee
    form_class = EmployeeForm
    extra_context = {'title': 'Edit Employee'}
    template_name = 'core/form.html'

    def get_success_url(self):
        return reverse('core:employee-detail', kwargs={'pk': self.object.pk})

class DeleteEmployeeView(DeleteView):
    """View for deleting an employee."""
    model = Employee
    template_name = 'core/employee-delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('core:employee-list')