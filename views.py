from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Constraint, Definition, Tableau


class IndexView(generic.ListView):
    model = Constraint
    template_name = 'otbank/index.html'
    context_object_name = 'constraint_list'


class ConstraintView(generic.DetailView):
    model = Constraint
    template_name = 'otbank/constraint.html'