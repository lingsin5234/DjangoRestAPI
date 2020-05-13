from django.db import models
from datetime import date as dt


class Project(models.Model):
    name = models.CharField(max_length=25)
    created_on = models.DateField(default=dt.today)

    def __str__(self):
        return str(self.name)


class Example(models.Model):
    name = models.CharField(max_length=25)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    created_on = models.DateField(default=dt.today)

    def __str__(self):
        return str(self.name) + ': ' + str(self.project)
