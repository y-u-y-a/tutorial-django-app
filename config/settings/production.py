from .base import *

# データベース
# GAEからアクセス
if os.getenv('GAE_APPLICATION', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'djangoApp',
            'USER': 'yuya',
            'PASSWORD': 'yuyadjangoapp',
            'HOST': '/cloudsql/djangoapp-262006:asia-northeast1:django-app',
        }
    }
    # ローカルからアクセス
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'djangoApp',
            'USER': 'yuya',
            'PASSWORD': 'yuyadjangoapp',
            'HOST': '127.0.0.1',
            'PORT': '3305'
        }
    }
