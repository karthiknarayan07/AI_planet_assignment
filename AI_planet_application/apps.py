from django.apps import AppConfig


class AiPlanetApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AI_planet_application'

    def ready(self):
        import AI_planet_application.signals