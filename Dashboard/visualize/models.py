from django.db import models

# Create your models here.
class MarketReport(models.Model):
    end_year = models.CharField(max_length=4, blank=True, null=True, default=None)
    intensity = models.IntegerField(blank=True, null=True, default=None)
    sector = models.CharField(max_length=100, blank=True, null=True, default=None)
    topic = models.CharField(max_length=100, blank=True, null=True, default=None)
    insight = models.TextField(blank=True, null=True, default=None)
    url = models.URLField(blank=True, null=True, default=None)
    region = models.CharField(max_length=100, blank=True, null=True, default=None)
    start_year = models.CharField(max_length=4, blank=True, null=True, default=None)
    impact = models.CharField(max_length=100, blank=True, null=True, default=None)
    added = models.DateTimeField(blank=True, null=True, default = None)
    published = models.DateTimeField(blank=True, null=True, default = None)
    country = models.CharField(max_length=100, blank=True, null=True, default=None)
    relevance = models.IntegerField(blank=True, null=True, default=None)
    pestle = models.CharField(max_length=100, blank=True, null=True, default=None)
    source = models.CharField(max_length=100, blank=True, null=True, default=None)
    title = models.TextField(blank=True, null=True, default=None)
    likelihood = models.IntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return self.title