import os  # Import the os module to manage environment variables

from celery import Celery  # Import Celery to handle background tasks

# Set the default Django settings module for the Celery application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Create a Celery instance with the project name ('core')
app = Celery("core", backend="redis://localhost")

# Load Celery configuration from Django settings with the 'CELERY' namespace
app.config_from_object("django.conf:settings", namespace="CELERY")

# Automatically discover and register tasks from all installed Django apps
app.autodiscover_tasks()
