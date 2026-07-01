from rest_framework.exceptions import NotFound, ValidationError

from apps.student.models import Student


class StudentService:

    @staticmethod
    def create(validated_data):

        cpf = validated_data["cpf"]

        if Student.objects.filter(cpf=cpf).exists():
            raise ValidationError(
                "CPF already registered."
            )

        student = Student.objects.create(**validated_data)

        return student

    @staticmethod
    def find_by_id(student_id):

        try:
            return Student.objects.get(id=student_id)

        except Student.DoesNotExist:
            raise NotFound(
                "Student not found."
            )

    @staticmethod
    def find_all():

        return Student.objects.all()

    @staticmethod
    def update(student_id, validated_data):

        student = StudentService.find_by_id(student_id)

        student.name = validated_data["name"]
        student.institution = validated_data["institution"]

        student.save()

        return student

    @staticmethod
    def delete(student_id):

        student = StudentService.find_by_id(student_id)

        student.delete()