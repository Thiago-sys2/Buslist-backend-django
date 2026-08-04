from rest_framework import serializers

from apps.attendance.models import Attendance
from apps.student.models import Student


class AttendanceUpdateSerializer(serializers.Serializer):

    studentId = serializers.PrimaryKeyRelatedField(
        quaryset = Student.objects.all(),
        source='student'
    )

    class Meta:
        model = Attendance
        fields = ['student_id', 'gift']