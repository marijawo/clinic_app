from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, FormView
from eclinic_app.models import *
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Class based views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from eclinic_app.forms import *

class PatientListView(ListView):
    model = Patient
    #context_object_name = 'all_patients'

    def get_context_data(self, **kwargs):
        context = super(PatientListView, self).get_context_data(**kwargs)
        context['all_patients'] = Patient.objects.all()
        context['all_visits'] = Visit.objects.all()
        return context

#class CreatePatient(CreateView):
#    model = Patient

class CreatePatientViewForm(FormView):
    template_name = "eclinic_app/patient_add.html"
    form_class = PatientForm
    success_url = '../../patients'

    def form_valid(self, form):
        form.save()
        return super(CreatePatientViewForm, self).form_valid(form)

class PatientDetailView(DetailView):
    queryset = Patient.objects.all()

    def get_object(self):
        #call super class
        object  = super(PatientDetailView, self).get_object()
        # record the last accessed date
        #   object.save()
        # return the object
        return object

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        context['all_patients'] = Patient.objects.all()
        context['all_visits'] = Visit.objects.all()
        return context

class PatientUpdate(UpdateView):
    model = Patient
    exclude = "patient_number"

class PatientDelete(DeleteView):
    model = Patient
    success_url = '/../patients'

class CreateVisitFormView(FormView):
    model = Visit
    template_name = "eclinic_app/visit_add.html"
    form_class = VisitForm
    success_url = "../../patients"

    def form_valid(self, form):
        form.save()
        return super(CreateVisitFormView, self).form_valid(form)