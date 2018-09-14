from django.http import HttpResponse
from django.views import generic

from django.db.models.query import EmptyQuerySet

from .models import Employee, EmployeeType

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'employees/index.html'
    context_object_name = 'latest_employee_list'

    def get_queryset(self):
        """
        Returns the a page set.
        """

        return Employee.objects.all()

