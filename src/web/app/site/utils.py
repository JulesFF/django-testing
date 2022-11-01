from django.conf import settings

import logging

from django.utils import timezone

logger = logging.getLogger(__name__)


def generateSecureRandomString(stringLength=10):
    """Generate a secure random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(password_characters) for i in range(stringLength))


def get_client_ip(request):
    """Extract the remote IP addr."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
