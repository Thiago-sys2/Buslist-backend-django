from rest_framework import serializers

from apps.student.models import Student


class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'cpf', 'institution']
    
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Name cannnot be blank."
            )
        
        return value
    
    def validate_institution(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Institution cannnot be blank."
            )
        
        return value

    def validate_cpf(self, value):
        if len(value) != 11:
            raise serializers.ValidationError(
                "CPF must have exactly 11 digits."
            )
        
        return value