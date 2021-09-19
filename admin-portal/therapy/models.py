from django.db import models
from clients.models import Client

# Create your models here.
class TherapyCenter(models.Model):
    title = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class Therapist(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    OT = models.IntegerField(choices=((1, "Yes"), (2, "No")))
    PT = models.IntegerField(choices=((1, "Yes"), (2, "No")))
    ST = models.IntegerField(choices=((1, "Yes"), (2, "No")))

    def __str__(self):
        return self.name


days = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
)


class TherapistSchedule(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    day = models.IntegerField(choices=days)
    start_time = models.TimeField()
    end_time = models.TimeField()
    therapy_center = models.ForeignKey(TherapyCenter, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.therapist}: {days[self.day-1][1]} ({self.start_time}-{self.end_time}) at {self.therapy_center}"


class TherapySlot(models.Model):
    title = models.CharField(null=True, blank=True, max_length=30)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    therapy_type = models.IntegerField(
        choices=((1, "OT"), (2, "PT"), (3, "ST")), null=True, blank=True
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(choices=((1, "Available"), (2, "Booked")), default=1)

    def __str__(self):
        return f"Therapist: {self.therapist}, Client: {self.client}, {self.date} ({self.start_time}-{self.end_time})"
