import string
import secrets

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from django.db.utils import IntegrityError
from django.utils.text import slugify

def generateSecureRandomString(stringLength:int=10) -> str:
    """ Generates a secure random string of letters, digits and special characters """
    password_characters =  string.digits + string.ascii_letters + string.digits
    return ''.join(secrets.choice(password_characters) for i in range(stringLength))


class Command(BaseCommand):
    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '-p',
            '--password',
            type=str,
            help='Password',
        )

        parser.add_argument(
            '-u',
            '--username',
            type=str,
            help='Username',
        )

    def handle(self, **options):
        # if password specified, then use it, otherwise generate random

        username = 'user'
        if options['username']:
            username = slugify(options['username'])
        email = None
        first_name = username

        self.stdout.write(f"creating user named '{username}'...", ending='\n')
        if options['password']:
            password = options['password']
        else:
            password = generateSecureRandomString(12)
            
        try:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name='User')

            # echo to output
            self.stdout.write(f"...user named '{username}' created with password '{password}'", ending='\n')
        except IntegrityError:
            self.stdout.write(f"...user named '{username}' already exists", ending='\n')