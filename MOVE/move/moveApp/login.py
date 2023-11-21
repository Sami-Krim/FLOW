from django.contrib.auth.backends import BaseBackend
from .models import Utilisateurs

class UtilisateursAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Utilisateurs.objects.get(username=username)
            if user.check_password(password):
                return user
        except Utilisateurs.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Utilisateurs.objects.get(pk=user_id)
        except Utilisateurs.DoesNotExist:
            return None
