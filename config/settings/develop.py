from .base import *

# データベース
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoApp',
        'USER': 'root',
        'PASSWORD': '',
    }
}
