from django.apps import AppConfig

class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'

    # PASTIKAN METHOD INI ADA DAN BENAR
    def ready(self):
        import catalog.signals