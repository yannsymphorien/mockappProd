import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_product_list_view():
    instance1 = test_helpers.create_product_product()
    instance2 = test_helpers.create_product_product()
    client = Client()
    url = reverse("product_product_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_product_create_view():
    type = test_helpers.create_type_type()
    client = Client()
    url = reverse("product_product_create")
    data = {
        "code": "text",
        "nameProduct": "text",
        "price": 1,
        "type": type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_product_detail_view():
    client = Client()
    instance = test_helpers.create_product_product()
    url = reverse("product_product_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_product_update_view():
    type = test_helpers.create_type_type()
    client = Client()
    instance = test_helpers.create_product_product()
    url = reverse("product_product_update", args=[instance.pk, ])
    data = {
        "code": "text",
        "nameProduct": "text",
        "price": 1,
        "type": type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
