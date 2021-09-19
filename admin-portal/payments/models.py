from django.db import models
from therapy.models import TherapySlot

# Create your models here.
class Payment(models.Model):
    amount = models.IntegerField(default=0)
    status = models.IntegerField(choices=((1, "Pending"), (2, "Paid")), default=1)
    therapy_slot = models.ForeignKey(TherapySlot, on_delete=models.CASCADE)

    def __str__(self):
        return f"Doctor: {self.therapy_slot.therapist} Patient: {self.therapy_slot.client} on {self.therapy_slot.date}  ({self.therapy_slot.start_time}-{self.therapy_slot.end_time})"
