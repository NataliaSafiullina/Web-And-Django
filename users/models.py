from django.db import models


class SearchingUsers(models.Model):
    ByName = models.CharField(max_length=100)
