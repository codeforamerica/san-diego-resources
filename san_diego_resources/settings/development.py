import dj_database_url
from san_diego_resources.settings.environment import *

DATABASES['default'] = dj_database_url.config(conn_max_age=600)
