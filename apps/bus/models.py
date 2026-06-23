from django.db import models

class Bus(models.Model):
    plate = models.CharField(max_length=20)
    capacity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'bus'

    def __str__(self):
        return self.plate