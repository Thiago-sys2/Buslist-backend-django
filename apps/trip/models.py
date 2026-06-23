from django.db import models

class TripPerdiod(models.TextChoices):
    MORNING = 'MORNING', 'Morning'
    AFTERNOON = 'AFTERNOON', 'Afternoon',
    NIGHT = 'NIGHT', 'Night'

class Trip(models.Model):
    date = models.DateField()

    period = models.CharField(
        max_length=20,
        choices=TripPerdiod.choices
    )

    #OneToMany e ManyToOne -> Só faz no lado do ManyToOne/Unilateral
    bus = models.ForeignKey(
        'bus.Bus',
        on_delete=models.CASCADE,
        related_name='trips'
    )

    class Meta:
        db_table = 'trips'

    def __str__(self):
        return f"(self.date) - {self.period}"
