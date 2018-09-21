# employees/models.py
from django.utils import timezone

from django.db import models


class EmployeeType(models.Model):
    """
    A model to record the types of employment roles.
    """
    CODE_TYPES = (
        ('STD','Standard'),
        ('MGR','Manager'),
        ('EXEC','Executive'),
        ('CHIEF','Chief Executive'),
    )
    code = models.CharField(max_length=5, choices=CODE_TYPES)
    text = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'role'

    def __str__(self):
        return self.code

class EmployeeManager(models.Manager):
    """
    Abstract out common logic for Employee model.
    """
    def get_managers(self):
        """
        filter on managers for query set.
        """
        return Employee.objects.filter(role__code='MGR')

class Employee(models.Model):
    """
    A model to record employee details.
    """
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    role = models.ForeignKey(EmployeeType, on_delete=models.SET_NULL, null=True, blank=True,)
    manager = models.ForeignKey('self', related_name='employee', on_delete=models.SET_NULL, null=True,  blank=True,)

    objects = EmployeeManager()

    class Meta:
        verbose_name_plural = 'staff'

    def __str__(self):
        return "<Employee: {} {}>".format(self.firstname, self.surname)


