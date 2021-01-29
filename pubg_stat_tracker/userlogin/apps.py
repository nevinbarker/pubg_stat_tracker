from django.apps import AppConfig


class UserloginConfig(AppConfig):
    name = 'userlogin'

    def ready(self):
        import userlogin.signals

