import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from type import models as type_models
from client import models as client_models
from product import models as product_models
from order import models as order_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_type_type(**kwargs):
    defaults = {}
    defaults["nameType"] = ""
    defaults.update(**kwargs)
    return type_models.type.objects.create(**defaults)
def create_client_client(**kwargs):
    defaults = {}
    if "user" not in kwargs:
        defaults["user"] = create_User()
    if "type" not in kwargs:
        defaults["type"] = create_type_type()
    defaults.update(**kwargs)
    return client_models.client.objects.create(**defaults)
def create_product_product(**kwargs):
    defaults = {}
    defaults["code"] = ""
    defaults["nameProduct"] = ""
    defaults["price"] = ""
    if "type" not in kwargs:
        defaults["type"] = create_type_type()
    defaults.update(**kwargs)
    return product_models.product.objects.create(**defaults)
def create_order_order(**kwargs):
    defaults = {}
    if "product" not in kwargs:
        defaults["product"] = create_product_product()
    if "client" not in kwargs:
        defaults["client"] = create_client_client()
    defaults.update(**kwargs)
    return order_models.order.objects.create(**defaults)
def create_order_offer(**kwargs):
    defaults = {}
    defaults["new_price"] = ""
    if "product" not in kwargs:
        defaults["product"] = create_product_product()
    defaults.update(**kwargs)
    return order_models.offer.objects.create(**defaults)
