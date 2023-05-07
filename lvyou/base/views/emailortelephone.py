from django.contrib.auth.models import User
from base.models.temp_tel_code import TempTelCode
from base.models.new_user import NewUser
import re


class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
            try:
                user = User.objects.get(**kwargs)
                if user.check_password(password):
                    return user
            # except User.DoesNotExist:
            except:
                return None

        if re.match("^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$", username):
            try:
                username = int(username)
                password = int(password)
                user = NewUser.objects.get(telephone=username, auth_code=password)
                return user
            except:
                return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
