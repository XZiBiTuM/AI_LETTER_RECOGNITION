from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai'

    def ready(self):
        try:
            import ai.signals
        except ImportError:
            print('Error!')
        else:
            print('Success!')
