from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length = 255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    address = models.TextField()
    created_by = models.ForeignKey(User,on_delete = models.CASCADE,related_name='patients')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctors')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patients')

    class Meta:
        unique_together = ('patient', 'doctor')

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"

