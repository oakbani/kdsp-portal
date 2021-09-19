from django.db import models
from clients.models import Client

# Create your models here.
class List(models.Model):
    date = models.DateTimeField()
    status = models.IntegerField(
        choices=(
            (1, "Pending"),
            (2, "Done"),
        ),
        default=1,
    )
    remarks = models.TextField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class WaitingListOT(List):
    def __str__(self):
        return f"{self.client}: {self.status}"

    pass


class WaitingListPT(List):
    def __str__(self):
        return f"{self.client}: {self.status}"

    pass


class WaitingListST(List):
    def __str__(self):
        return f"{self.client}: {self.status}"

    pass


class MasterList(List):
    def __str__(self):
        return f"{self.client}: {self.status}"

    pass
