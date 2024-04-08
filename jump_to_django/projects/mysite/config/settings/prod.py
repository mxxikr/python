from .base import *

ALLOWED_HOSTS = ['3.34.35.120', 'mxxikr.com']
STATIC_ROOT = BASE_DIR / 'static/'
# STATICFILES_DIRS 리스트에 STATIC_ROOT와 동일한 디렉터리가 포함되어 있으면 서버 실행 시 오류 발생
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'bx,Poz*^-UR0fsu+1b!nS8H~u92zmkoP',
        'HOST': 'ls-6c766010bbcad991d82c77e6e05bd1e324eba434.cfhwbq4nxsyb.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}