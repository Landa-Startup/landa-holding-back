from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

# from .signals import custom_signal
# from django.core.cache import cache

# def send_data_to_view(sender, data, **kwargs):
#     # Process the data and do something with it in the view
#     print(data)
#     cache.set('custom_data', data)


# custom_signal.connect(send_data_to_view)
