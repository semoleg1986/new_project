from django.contrib.auth.models import User
from .models import Profile

class EmailAuthBackend(object):
    def authenticate(self, request, username=None, passsword=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(passsword):
                return user
            return None
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
