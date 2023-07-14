import os
import sys
import django
from django.contrib.auth.management.commands.createsuperuser import get_user_model

# Add the parent directory of 'mysite' to the Python path
sys.path.append('/app')

# Set the settings module for Django. Change 'mysite.settings' to your actual settings module if it's different.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# Set up the Django environment.
django.setup()

# Create the superuser.
get_user_model()._default_manager.db_manager('default').create_superuser(
    username=os.getenv('DJANGO_SU_NAME'),
    email=os.getenv('DJANGO_SU_EMAIL'),
    password=os.getenv('DJANGO_SU_PASSWORD')
)