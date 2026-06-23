from rest_framework import serializers

from apps.student.models import Student

class StudentResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            'id'
            'name',
            'cpf',
            'institution'
        ]