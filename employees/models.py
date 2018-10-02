# employees/models.py
import logging

from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

logger = logging.getLogger(__name__)


class EmployeeType(models.Model):
    """
    A model to record the types of employment roles.
    """
    CODE_TYPES = (
        ('STD', 'Standard'),
        ('MGR', 'Manager'),
        ('EXEC', 'Executive'),
        ('CHIEF', 'Chief Executive'),
    )
    code = models.CharField(max_length=5, choices=CODE_TYPES,)
    text = models.CharField(max_length=100,)

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
    firstname = models.CharField(max_length=100,)
    surname = models.CharField(max_length=100,)
    start_date = models.DateTimeField(default=timezone.now,)
    role = models.ForeignKey(EmployeeType, on_delete=models.SET_NULL, null=True, blank=True,)
    manager = models.ForeignKey('self', related_name='employee', on_delete=models.SET_NULL, null=True,  blank=True,)

    objects = EmployeeManager()

    # Internal Properties

    @property
    def role_title(self):
        """
        Employee role title
        """
        _title = self.role.text

        if self.role.code == 'EXEC':
            _title = 'General Manager'

        return _title

    class Meta:
        verbose_name_plural = 'staff'

    def __str__(self):
        return "<Employee: {} {}>".format(self.firstname, self.surname)


class EmployeeListener(object):
    """
    Event Listener for Employee object.
    """
    @staticmethod
    @receiver(post_save, sender=Employee)
    def saving_employee(sender, instance, **kwargs):
        logger.debug("Details saved through a signal %s %s", sender, instance)


class ApplicationRequest(models.Model):
    subject = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)
    officer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()


class IDRequest(ApplicationRequest):
    REASON_CHOICES = (('missing', 'There is currently no Photographic Identification uploaded'),
                      ('expired', 'The current identification has expired'),
                      ('not_recognised',
                       'The current identification is not recognised by the Department of Parks and Wildlife'),
                      ('illegible', 'The current identification image is of poor quality and cannot be made out.'),
                      ('other', 'Other'))
    reason = models.CharField('Reason', max_length=30, choices=REASON_CHOICES, default=REASON_CHOICES[0][0])


class ReturnsRequest(ApplicationRequest):
    REASON_CHOICES = (('outstanding', 'There are currently outstanding returns for the previous licence'),
                      ('other', 'Other'))
    reason = models.CharField('Reason', max_length=30, choices=REASON_CHOICES, default=REASON_CHOICES[0][0])


class AmendmentRequest(ApplicationRequest):
    STATUS_CHOICES = (('requested', 'Requested'), ('amended', 'Amended'))
    REASON_CHOICES = (('insufficient_detail', 'The information provided was insufficient'),
                      ('missing_information', 'There was missing information'),
                      ('other', 'Other'))
    status = models.CharField('Status', max_length=30, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    reason = models.CharField('Reason', max_length=30, choices=REASON_CHOICES, default=REASON_CHOICES[0][0])


class Assessment(ApplicationRequest):
    STATUS_CHOICES = (('awaiting_assessment', 'Awaiting Assessment'), ('assessed', 'Assessed'),
                      ('assessment_expired', 'Assessment Period Expired'))
    assigned_assessor = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    date_last_reminded = models.DateField(null=True, blank=True)
    comment = models.TextField(blank=True)
    purpose = models.TextField(blank=True)


