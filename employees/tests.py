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
        test_employee = Employee.objects.create(firstname="Test", surname="Case")
        test_employee.role = EmployeeType.objects.create(code="MGR")
        test_employee.save()

        EmployeeType.objects.create(code="SUPER", text="Supervisor")
        EmployeeType.objects.create(code="EXEC")

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
        test_employee = Employee.objects.create(firstname="Margaret", surname="Peters")
        test_employee.role = EmployeeType.objects.create(code="MGR")
        test_employee.save()

        # Check total count of 2 managers stored.
        self.assertEqual(Employee.objects.get_managers().count(),2)

    def test_employee_gender(self):
        """
        Assert persistance of employee gender.
        """
        test_employee = Employee.objects.get(surname="Case")
        test_employee.gender = "M"
        test_employee.save()

        self.assertEqual(test_employee.gender, "M")
