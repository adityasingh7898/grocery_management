from django.apps import AppConfig


<<<<<<<< HEAD:Admin_app/apps.py
class AdminAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Admin_app'
========
class CustomerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer_app'
>>>>>>>> 91f0e756d322337d43d638efe1bc27501be6fda6:customer_app/apps.py
