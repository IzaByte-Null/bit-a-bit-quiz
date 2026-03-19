from dotenv import load_dotenv 
import os
from pathlib import Path
from datetime import timedelta 

load_dotenv() # for .env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!| segurança 
SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key_para_dev') # para o render

#configuração de ambiente for RENDER
IS_RENDER_DEPLOYMENT = os.environ.get('RENDER') == 'true' 

if IS_RENDER_DEPLOYMENT:
    DEBUG = False
    ALLOWED_HOSTS = ['bit-a-bit-quiz-1.onrender.com', '.onrender.com']
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
else:
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY') 
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:5500", 
    ]
    


# Application definition
INSTALLED_APPS = [
    'usuarios',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'quiz', 
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_api.urls'

WSGI_APPLICATION = 'backend_api.wsgi.application'

# ARQUIVOS ESTATICOS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# STATIC FILES
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# Local onde os arquivos serão coletados | collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Gerenciamento de arquivos de midia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Autenticaçao e Segurança
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

# Password validation 
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CONFIGURAÇÃO DE EMAIL e REDIRECIONAMENTO 
DEFAULT_FROM_EMAIL = 'suportebitabit1@gmail.com'
LOGIN_REDIRECT_URL = '/principal/'
LOGOUT_REDIRECT_URL = '/login/'


# CSRF_TRUSTED_ORIGINS de segurança
CSRF_TRUSTED_ORIGINS = [
    'https://bit-a-bit-quiz.onrender.com',
    'https://*.onrender.com'
]


# SUBINDO SITE PARA O SERVIDOR/ IMPORTAÇÕES DE DADOS 

# DATABASE_URL para DBD_NEON
DATABASE_URL = os.environ.get("DBD_NEON") 

if DATABASE_URL: 
    import dj_database_url 
    DATABASES = { 
        "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=600) 
    } 
else: 
    DATABASES = { 
        'default': { 
            'ENGINE': 'django.db.backends.sqlite3', 
            'NAME': BASE_DIR / 'db.sqlite3', 
        } 
    }