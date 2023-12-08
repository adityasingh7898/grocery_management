from django.apps import AppConfig

class AdminAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Admin_app'
    
class CustomerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer_app'
