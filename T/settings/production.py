from .base import *
import dj_database_url





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd25ck31jvd4p8m',
        'USER': 'prtjluvdnhsanj',
        'PASSWORD': 'c6d93658711194e815a70abe33fa912978508ec16550b89b6f7285e76906e9fc',
        'HOST': 'ec2-23-21-204-166.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# DATABASES['default'] =  dj_database_url.config(default=os.getenv('DATABASE_URL'))

