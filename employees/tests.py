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
        EmployeeType.objects.create(code="MGR")
        logger.info('Set up DB with an Employee object')

    def test_employee_type_creation(self):
        """
        Assert the creation of a new Employee Type.
        """
        EmployeeType.objects.create(code="SUPER", text="Supervisor")
        et = EmployeeType.objects.get(code="SUPER")
        logger.info('Employee Type: %s', et.code)
        self.assertTrue(isinstance(et, EmployeeType))

    def test_employee_creation(self):
        """ 
        An Employee details is persisted. 
        """
        Employee.objects.filter(firstname="Test").update(firstname="Fred")
        e = Employee.objects.get(firstname="Fred")
        logger.info('updates: %s', e.firstname)
#        self.assertTrue(isinstance(r, EmployeeType))

    def tes_employee_get_managers(self):
        """
        Assert retrieval of Managers.
        """
        e = Employee.objects.get_managers()
        logger.info('Role retrieved:')
#        self.assertTrue(isinstance(e, Employee))
