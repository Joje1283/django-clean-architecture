from django.db import models


class Report(models.Model):
    data = models.TextField(max_length=200)