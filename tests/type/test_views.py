import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_type_list_view():
    instance1 = test_helpers.create_type_type()
    instance2 = test_helpers.create_type_type()
    client = Client()
    url = reverse("type_type_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_type_create_view():
    client = Client()
    url = reverse("type_type_create")
    data = {
        "nameType": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_type_detail_view():
    client = Client()
    instance = test_helpers.create_type_type()
    url = reverse("type_type_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_type_update_view():
    client = Client()
    instance = test_helpers.create_type_type()
    url = reverse("type_type_update", args=[instance.pk, ])
    data = {
        "nameType": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
