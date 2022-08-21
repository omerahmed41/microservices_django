
from django.db import transaction
import logging

from Client.models import Client

logger = logging.getLogger()


@transaction.atomic
def create_client(user, first_name, last_name, client_type=Client.B2C_TYPE, phone_number_data=None):

    client, created = Client.objects.get_or_create(
        user=user, first_name=first_name, last_name=last_name,
        client_type=client_type, contact_preference=phone_number_data)

    return client, created

