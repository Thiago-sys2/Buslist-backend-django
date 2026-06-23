from rest_framework import serializers
from apps.attendance.models import Attendance

class AttendanceResponseSerializer(serializers.ModelSerializer):

    student_id = serializers.IntegerField(
        source='student.id'
    )

    name_student = serializers.CharField(
        source='student.name'
    )

    institution = serializers.CharField(
        source='student.institution'
    )

    class Meta:
        model = Attendance
        fields = [
            'student_id',
            'name_student',
            'institution',
            'gift'
        ]