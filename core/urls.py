from django.urls import path
from core import views
import django.contrib.auth.views as auth_views

app_name = 'core'

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='core/login.html',
            redirect_authenticated_user=True,
        ),
        name='login'
    ),
    path('logout/', auth_views.logout_then_login, name='logout'),

    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('add-employee/', views.AddEmployeeView.as_view(), name='add-employee'),
    path('employee/<pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/<pk>/edit/', views.EditEmployeeView.as_view(), name='edit-employee'),
    path('edit-salary/<pk>/', views.EditSalaryView.as_view(), name='edit-salary'),
    path('delete-employee/<pk>/', views.DeleteEmployeeView.as_view(), name='delete-employee'),
]