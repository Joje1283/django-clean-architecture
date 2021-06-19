from django.db import models


class Report(models.Model):
    data = models.JSONField(max_length=200)
