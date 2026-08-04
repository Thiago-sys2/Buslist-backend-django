from core.exceptions.user_exceptions import UserNotFoundException, EmailAlreadyExistsException

from apps.user.models import User, UserRole

class UserService:

    @staticmethod
    def create(validated_data):

        email = validated_data["email"].strip().lower()

        if User.objects.filter(email=email).exists():
            raise EmailAlreadyExistsException()
        
        user = User(
            name = validated_data["name"].strip(),
            email=email,
            role=UserRole.USER
        )

        user.set_password(validated_data["password"])

        user.save()

        return user
    
    @staticmethod
    def find_all():

        return User.objects.all()
    
    @staticmethod
    def find_by_id(user_id: int) -> User:

        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise UserNotFoundException()

    @staticmethod
    def update(user_id: int, validated_data: dict) -> User:

        user = UserService.find_by_id(user_id)

        if "name" in validated_data:
            user.name = validated_data["name"].strip()

        if "email" in validated_data:

            email = validated_data["email"].strip().lower()

            if User.objects.exclude(id=user.id).filter(email=email).exists():
                raise EmailAlreadyExistsException()
            
            user.email = email

        user.save()

        return user
    
    @staticmethod
    def delete(user_id):

        user = UserService.find_by_id(user_id)

        user.delete()
    
