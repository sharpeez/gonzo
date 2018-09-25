import logging

from django.test import TestCase

from .models import Employee, EmployeeType


logger = logging.getLogger(__name__)

class EmployeeModelTest(TestCase):
    """
    Test suite relating to the Employee Model.
    """

    def setUp(self):
        """
        Set up context for unit test.
        """
        Employee.objects.create(firstname="Test", surname="Case")
        EmployeeType.objects.create(code="SUPER", text="Supervisor")
        Employee.objects.filter(firstname="Test").update(role=EmployeeType.objects.create(code="MGR"))

    def test_employee_type_creation(self):
        """
        Assert the creation of a new Employee Type.
        """
        EmployeeType.objects.create(code="STD")

        # Check new EmployeeType is created.
        self.assertTrue(isinstance(EmployeeType.objects.get(code="STD"), EmployeeType))

    def test_employee_creation(self):
        """ 
        An Employee details is persisted. 
        """
        Employee.objects.filter(firstname="Test").update(role=EmployeeType.objects.get(code="SUPER"))

        # Check new employee is created.
        self.assertTrue(isinstance(Employee.objects.get(surname="Case"), Employee))

    def test_employee_get_managers(self):
        """
        Assert retrieval of Managers.
        """
        Employee.objects.create(firstname="Margaret", surname="Peters")
        Employee.objects.filter(firstname="Margaret").update(role=EmployeeType.objects.create(code="MGR"))

        # Check total count of 2 managers stored.
        self.assertEqual(Employee.objects.get_managers().count(),2)
