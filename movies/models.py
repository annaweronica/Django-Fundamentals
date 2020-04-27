from django.db import models

class Movie(models.Model):

    title = models.CharField("Movie Title", max_length=100, null=True, blank=False)
    synopsis = models.CharField("Synopsis", max_length=100, null=False, blank=False)
    realese_year = models.CharField("Realse_year", max_length=100, null=False, blank=False)
    duration = models.IntegerField("Duration", blank=True, default=10, null=True)
    

