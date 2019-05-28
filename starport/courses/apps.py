from django.apps import AppConfig

class CoursesConfig(AppConfig):
    name = 'courses'

    def ready(self):
        # importing model classes
        from .signals import cs_approved_signal
