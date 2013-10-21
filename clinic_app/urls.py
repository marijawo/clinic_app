from django.conf.urls import patterns, include, url

from eclinic_app.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^patients/$', PatientListView.as_view(), name='patient-view'),
    url(r'^patient-detail/(?P<pk>\d+)/$', PatientDetailView.as_view(), name='patient-detail'),
    url(r'^patient/add/', CreatePatientViewForm.as_view(), name='create-patient'),

    url(r'visit/(?P<pk>\d+)/$', PatientUpdate.as_view(), name='patient_update'),
    url(r'patient/(?P<pk>\d+)/delete/$', PatientDelete.as_view(), name='patient_delete'),

    # Visit URLS
    url(r'^visit/add/$', CreateVisitFormView.as_view(), name='add_visit'),


    # url(r'^district-form/$', DistrictFormView),
    url(r'^admin/', include(admin.site.urls)),
)