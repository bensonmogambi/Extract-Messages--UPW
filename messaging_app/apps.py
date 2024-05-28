from django.apps import AppConfig


class MessagingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messaging_app'
    verbose_name = 'Messaging Application'

    def ready(self):
        # Import signals or other initialization code here if needed
        import messaging_app.signals  # Example if you are using Django signals
