import logging
import json
import time
from datetime import datetime, date, timedelta

from django.utils import timezone
from django.apps import apps
from django.conf import settings

logger = logging.getLogger(__name__)
