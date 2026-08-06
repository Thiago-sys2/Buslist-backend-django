from django.core.management.base import BaseCommand

from apps.user.models import User, UserRole


class Command(BaseCommand):

    help = "Promotes a user to ADMIN."

    def add_arguments(self, parser):

        parser.add_argument(
            "email",
            type=str,
            help="User email."
        )

    def handle(self, *args, **options):

        email = options["email"]

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:

            self.stdout.write(
                self.style.ERROR("User not found.")
            )

            return

        user.role = UserRole.ADMIN
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"{user.email} is now ADMIN."
            )
        )