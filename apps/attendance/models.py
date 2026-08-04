from django.db import models


class Attendance(models.Model):
    gift = models.BooleanField(default=False)

    trip = models.ForeignKey(
        'trip.Trip',
        on_delete=models.CASCADE,
        null=False,
        related_name='attendances'
    )
    
    student = models.ForeignKey(
        'student.Student',
        on_delete=models.CASCADE,
        null=False,
        related_name='attendances'
    )

    class Meta:
        db_table = 'attendances'

    def __str__(self):
        return f"{self.student} - {self.trip}"