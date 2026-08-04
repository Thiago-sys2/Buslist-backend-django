from django.db import models


class Bus(models.Model):
    id = models.AutoField(primary_key=True)

    plate = models.CharField(max_length=20)
    capacity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'bus'

    def __str__(self):
        return f"{self.plate} - Capacity: {self.capacity} - Active: {self.active}"