from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self): #deals with signal to create a profile for the user upon creation of the user
        import users.signals 
