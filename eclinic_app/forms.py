from django.forms import ModelForm
from eclinic_app.models import *

class PatientForm(ModelForm):
    class Meta:
        model = Patient

class VisitForm(ModelForm):
    class Meta:
        model = Visit

class DistrictForm(ModelForm):
    class Meta:
        model = District

class RegionForm(ModelForm):
    class Meta:
        model = Region

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor

class NurseForm(ModelForm):
    class Meta:
        model = Nurse

class PaymentForm(ModelForm):
    class Meta:
        model = Payment

class CashierForm(ModelForm):
    class Meta:
        model = Doctor
