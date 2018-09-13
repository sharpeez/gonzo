import datetime
import logging

from django.db import models
from django.utils import timezone

logger = logging.getLogger('polls')

# Create your models here.

class Question(models.Model):
    """ A model to record questions for polling.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    logger.info('Question model contains ordering {} was_published_recently'.format(was_published_recently))
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text

class CoolQuestion(Question):
    pass


class Choice(models.Model):
    """ A model to record choices for polling.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

