from rest_framework import serializers


class StudentRegisterSerializer(serializers.Serializer):

    name = serializers.CharField()
    cpf = serializers.CharField(min_length=11, max_length=11)
    institution = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True
    )

    def validate_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Name cannot be blank."
            )

        return value

    def validate_institution(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Institution cannot be blank."
            )

        return value
