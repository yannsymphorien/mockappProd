import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_client_list_view():
    instance1 = test_helpers.create_client_client()
    instance2 = test_helpers.create_client_client()
    client = Client()
    url = reverse("client_client_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_client_create_view():
    user = test_helpers.create_User()
    type = test_helpers.create_type_type()
    client = Client()
    url = reverse("client_client_create")
    data = {
        "user": user.pk,
        "type": type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_client_detail_view():
    client = Client()
    instance = test_helpers.create_client_client()
    url = reverse("client_client_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_client_update_view():
    user = test_helpers.create_User()
    type = test_helpers.create_type_type()
    client = Client()
    instance = test_helpers.create_client_client()
    url = reverse("client_client_update", args=[instance.pk, ])
    data = {
        "user": user.pk,
        "type": type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
