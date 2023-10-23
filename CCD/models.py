from django.db import models
from django.db.models import DateField, TextField, CharField, URLField, IntegerField
from django.template.defaultfilters import truncatechars


class NewsMonitoring(models.Model):
    date = DateField()
    description = TextField(blank=True)
    area_tag = CharField(max_length=255, blank=True)
    topic_tag = CharField(max_length=255, blank=True)
    link = URLField(blank=True)
    source = CharField(max_length=255, blank=True)
    source_tag = CharField(max_length=255, blank=True)
    subject = CharField(max_length=255, blank=True)
    additional_info = CharField(max_length=255, blank=True)
    type_of_threat = CharField(max_length=255, blank=True)
    evaluation = CharField(max_length=255, blank=True)
    grand_narrative = CharField(max_length=255, blank=True)
    narrative = CharField(max_length=255, blank=True)
    status = CharField(max_length=255, blank=True)
    suggestions_for_response = CharField(max_length=255, blank=True)
    country = CharField(max_length=255, blank=True)
    ua_region = CharField(max_length=255, blank=True)
    index = IntegerField()

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

