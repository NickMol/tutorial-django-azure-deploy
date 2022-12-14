import os

from django.core.wsgi import get_wsgi_application

# Check for the PRODUCTION environment variable to see if we are running in Azure Ap Service
# If so, then load the settings from production.py
settings_module = 'azure_project.production' if 'PRODUCTION' in os.environ else 'azure_project.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)


application = get_wsgi_application()
