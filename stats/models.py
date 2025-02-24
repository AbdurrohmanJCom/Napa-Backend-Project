from django.db import models
from django.utils import timezone

class UserStats(models.Model):
    date = models.DateField()
    registered_users = models.IntegerField(default=0)
    last_updated = models.DateTimeField(null=True, blank=True)

class OrderStats(models.Model):
    date = models.DateField()
    created_orders = models.IntegerField(default=0)
    last_updated = models.DateTimeField(null=True, blank=True)

class ProposalStats(models.Model):
    date = models.DateField()
    created_proposals = models.IntegerField(default=0)
    last_updated = models.DateTimeField(null=True, blank=True)
