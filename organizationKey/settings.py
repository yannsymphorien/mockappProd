from rest_framework_api_key.models import *
from rest_framework_api_key.permissions import BaseHasAPIKey, KeyParser

class BearerKeyParser(KeyParser):
    keyword = "Bearer"

class HasAPIKey(BaseHasAPIKey):
    model = APIKey  # Or a custom model
    key_parser = BearerKeyParser()