

# Register your models here.
from django.contrib import admin
from schedule.models import Calendar # type: ignore

from .models import Doctor, Patient, Appointment

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)



