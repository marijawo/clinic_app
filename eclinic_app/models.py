from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

STAFF_TYPE = enumerate(("Cashier", "Staff", "Doctor", "Nurse", "Cleaner", "Security"))

class Patient(models.Model):
    patient_number = models.CharField(max_length=6, unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.BooleanField()
    address = models.CharField(max_length=80)
    district = models.ForeignKey('District')
    region = models.ForeignKey('Region')
    telephone = models.CharField(max_length=9)
    #photo = models.ImageField(upload_to='photos', null=True, blank=True)

    class Meta:
        ordering = ['patient_number']

    def get_patient_age(self):

        born_day = self.date_of_birth
        age = 2013 - born_day
        return age

    def get_middle_name(self):
        if self.middle_name == '':
            return '---'
        else:
            return self.middle_name

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})

    def get_full_name(self):
        return u'%s %s %s' %(self.first_name, self.middle_name, self.last_name)

    def get_gender(self):
        if self.gender == False:
            return "Male"
        else:
            return "Female"

    def get_total_patients(self):
        total_patient = Patient.objects.all().count();
        return total_patient

    def get_all_male_patients(self):
        all_male = Patient.objects.filter(gender = False).count()
        return all_male

    def get_all_female_patients(self):
        all_female = Patient.objects.filter(gender = True).count()
        return all_female

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (self.first_name, self.middle_name, self.last_name, self.address, self.telephone)

class District(models.Model):
    name = models.CharField(max_length=50)

    def get_total_district(sel):
        total_districts = District.objects.all().count()
        return total_districts

    def __unicode__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=80)

    def get_total_regions(sel):
        total_regions = Region.objects.all().count()
        return total_regions

    def __unicode__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    telephone = models.CharField(max_length=9)

    def get_absolute_url(self):
        return reverse('doctor-detail', kwargs={'pk': self.pk})

    def get_full_doctor_name(self):
        return u'%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (
            self.first_name, self.middle_name, self.last_name, self.address, self.telephone)


class Nurse(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    telephone = models.CharField(max_length=9)

    def get_absolute_url(self):
        return reverse('nurse-detail', kwargs={'pk': self.pk})

    def get_full_nurse_name(self):
        return u'%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (
            self.first_name, self.middle_name, self.last_name, self.address, self.telephone)


class Visit(models.Model):
    patient = models.ForeignKey('Patient')
    screened_by = models.ForeignKey('Nurse')
    date_visit = models.DateField()
    remarks = models.TextField()
    seen_by_dr = models.ForeignKey('Doctor')

    def get_absolute_url(self):
        return reverse('visit-detail', kwargs={'pk': self.pk})

    def get_total_visits(sel):
        total_visits = Visit.objects.all().count()
        return total_visits

    class Meta:
        get_latest_by = "date_visit"

    def __unicode__(self):
        return u'%s, %s, %s, %s %s' % (self.patient, self.remarks, self.screened_by, self.seen_by_dr, self.date_visit)

class Payment(models.Model):
    patient = models.ForeignKey('Patient')
    amount = models.IntegerField(default=0)
    paid_for = models.TextField()
    paid_to = models.ForeignKey('Cashier')

    def get_absolute_url(self):
        return reverse('payment-deail', kwargs={'pk': self.pk})

    def get_total_payments(self):
        total_payments = Patient.objects.all().count()
        return total_payments

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.patient, self.amount, self.paid_for, self.paid_to)

class Cashier(models.Model):
    patient = models.ForeignKey(Payment)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    telephone = models.CharField(max_length=9)

    def get_absolute_url(self):
        return reverse('cashier-detail', kwargs={'pk': self.pk})

    def get_cashier_full_name(self):
        return u'%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (
            self.first_name, self.middle_name, self.last_name, self.address, self.telephone)