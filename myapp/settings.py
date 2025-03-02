import os
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Basic Django settings
SECRET_KEY = os.getenv('SECRET_KEY', 'EnxoPualfqeepgFngBrdPUcXJRJjA-cMefv-WNtj4F4bs0Ucrwks50J7B_riULXR1Vg')
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Add your app here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

# Add more settings as necessary (e.g., for authentication, logging, etc.)

# Set SECRET_KEY from environment variable
SECRET_KEY = env('SECRET_KEY', default='EnxoPualfqeepgFngBrdPUcXJRJjA-cMefv-WNtj4F4bs0Ucrwks50J7B_riULXR1Vg')

