from django.apps import AppConfig

class CoursesConfig(AppConfig):
    name = 'courses'

    def ready(self):
        # importing model classes
        from .gh_factory import cs_approved_signal