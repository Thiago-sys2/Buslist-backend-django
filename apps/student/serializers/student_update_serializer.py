from rest_framework import serializers

from apps.student.models import Student

class StudentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'institution']

    def validate_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Name cannnot be blank."
            )
        
        return value

    def validate_institution(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Institution cannnot be blank."
            )
        
        return value