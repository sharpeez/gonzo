from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.query import EmptyQuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Employee, EmployeeType

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'employees/index.html'
    context_object_name = 'latest_employee_list'
    paginate_by = 20
    queryset = Employee.objects.all()
