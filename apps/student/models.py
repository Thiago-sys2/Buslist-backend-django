from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    institution = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'students'

    def __str__(self):
        return f"{self.name} - {self.cpf}"
