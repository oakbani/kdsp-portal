from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    address = models.CharField(blank=True, max_length=100)
    cnic = models.CharField(blank=True, max_length=15)
    contact = models.CharField(max_length=15)
    status = models.IntegerField(
        choices=((1, "Ineligible"), (2, "Enrolled"), (3, "UnEnrolled")), default=3
    )

    def __str__(self):
        return self.name
