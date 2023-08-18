from pathlib import Path
import os, json
from django.urls import reverse_lazy
import socket



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# secrets.json 파일에 넣었음


#* secrets 파일 불러오기 - 배포 오류로 secrets.json 내용을 settings 파일에 명시 
# secret_file = os.path.join(BASE_DIR, 'secrets.json') 
SECRET_KEY = "django-insecure-57^tohc!v_cbvfwndk#!)=t-9)1)cd40!@1^i69z3%#@28%(=y"
EMAIL_HOST_USER="saviorservice2023@gmail.com",
EMAIL_HOST_PASSWORD="rackvwohuuubvqns"



#* You're accessing the development server over HTTPS, but it only supports HTTP. 오류 해결
if socket.gethostname()=="Raouf-PC":
    from local_settings import *


# with open(secret_file) as f:
#     secrets = json.loads(f.read())

# def get_secret(setting, secrets=secrets):
#     try:
#         return secrets[setting]
#     except KeyError:
#         error_msg = "Set the {} environment variable".format(setting)
#         raise ImproperlyConfigured(error_msg)

# SECRET_KEY = get_secret("SECRET_KEY")
SECRET_KEY = "django-insecure-57^tohc!v_cbvfwndk#!)=t-9)1)cd40!@1^i69z3%#@28%(=y"





# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'savior',
    'accounts',
    'admin_thumbnails',
    'rest_framework',
    
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

ROOT_URLCONF = 'h_thon.urls'

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

WSGI_APPLICATION = 'h_thon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/


LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 커스텀된 user 
AUTH_USER_MODEL = 'users.User'

# #* 이메일 비밀번호 재설정
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# 메일을 보내는 호스트 서버
EMAIL_HOST = 'smtp.gmail.com'

# ENAIL_HOST에 정의된 SMTP 서버가 사용하는 포트 gmail 용(587: TLS/STARTTLS용 포트)
EMAIL_PORT = '587'

#  발신할 이메일 주소 '~@gmail.com'  (숨겨야 하는 값이기에 env로 표현)
# EMAIL_HOST_USER = ("EMAIL_HOST_USER")
EMAIL_HOST_USER="saviorservice2023@gmail.com"


# 발신할 이메일 비밀번호 (2단계 인증일경우 앱 비밀번호)
# EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
# EMAIL_HOST_PASSWORD = ("EMAIL_HOST_PASSWORD")
EMAIL_HOST_PASSWORD="rackvwohuuubvqns"


# 발신 메일 내용 https로 바꾸기
# SECURE_SSL_REDIRECT = True


# TLS 보안 방법 (SMPT 서버와 통신할 떄 TLS (secure) connection 을 사용할지 말지 여부)
EMAIL_USE_TLS = True

# 사이트와 관련한 자동응답을 받을 이메일 주소
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#* 카카오 로그인 
# KAKAO_CONFIG = {
#     "KAKAO_REST_API_KEY": "190d42e2a674395e7a82755e907fcba9",   
#     # "KAKAO_REDIRECT_URI": "http://localhost:8000/accounts/kakao/login/callback/",
#     "KAKAO_CLIENT_SECRET_KEY": "58aYr20LxBJuTFqW4yZbeAMWLqAnXMdx", 
# }

# KAKAO_REST_API_KEY= "190d42e2a674395e7a82755e907fcba9"
# # KAKAO_REDIRECT_URI= "http://localhost:8000/accounts/kakao/login/callback/"
# KAKAO_REDIRECT_URI= "http://127.0.0.1:8000/accounts/kakao/login/callback"
# KAKAO_CLIENT_SECRET_KEY= "58aYr20LxBJuTFqW4yZbeAMWLqAnXMdx"

KAKAO_REST_API_KEY="190d42e2a674395e7a82755e907fcba9" # 앱 생성시 발급받은 rest api
KAKAO_ID="190d42e2a674395e7a82755e907fcba9" # 앱 생성시 발급받은 rest api
KAKAO_SECRET="58aYr20LxBJuTFqW4yZbeAMWLqAnXMdx" # client secret key
