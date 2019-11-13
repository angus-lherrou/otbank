from django.db import models


"""
class Subfield(models.Model):
    subfield_name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.subfield_name
"""


class Constraint(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


class Definition(models.Model):
    constraint = models.ForeignKey(Constraint, on_delete=models.CASCADE)
    definition_text = models.CharField(max_length=1000)
    definition_citation = models.CharField(max_length=1000)
    ''' first definition should be explicitly called as true '''
    primary = models.BooleanField(default=False)

    def __str__(self):
        return self.definition_text


class Tableau(models.Model):
    tab_constraints = models.ManyToManyField(Constraint)
    code = models.CharField(max_length=1000)
    tab_citation = models.CharField(max_length=1000)

    def __str__(self):
        return self.code
