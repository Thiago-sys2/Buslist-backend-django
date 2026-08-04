from django.contrib.auth.backends import BaseBackend

from apps.user.models import User


class EmailAuthenticationBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):

        if email is None or password is None:
            return None

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None