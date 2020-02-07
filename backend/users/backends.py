from users.models import CustomUser
# from django.contrib.auth.backends import BaseBackend
import logging


class MyAuthBackend(object):
    def authenticate(self, request, email, password):
        try:
            user = CustomUser.objects.get(email=email)

            if user.check_password(password):
                return user
            else:
                return None
        except CustomUser.DoesNotExist:
            logging.getLogger("error_logger").error(
                "user with login %s does not exists " % email)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(sys_id=user_id)
            if user:
                return user
            return None
        except CustomUser.DoesNotExist:
            logging.getLogger("error_logger").error(
                "user with %(user_id)d not found")
            return None
