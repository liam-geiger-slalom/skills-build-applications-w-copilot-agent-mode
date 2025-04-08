from django.core.management import call_command
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

# Call the populate_db command
try:
    call_command('populate_db')
    print("populate_db command executed successfully.")
except Exception as e:
    print(f"Error executing populate_db command: {e}")
