import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = 'media'
MEDIA_PATH = "{}/{}".format(BASE_DIR, MEDIA_ROOT)
