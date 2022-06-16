import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_order_list_view():
    instance1 = test_helpers.create_order_order()
    instance2 = test_helpers.create_order_order()
    client = Client()
    url = reverse("order_order_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_order_create_view():
    product = test_helpers.create_product_product()
    client = test_helpers.create_client_client()
    client = Client()
    url = reverse("order_order_create")
    data = {
        "product": product.pk,
        "client": client.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_order_detail_view():
    client = Client()
    instance = test_helpers.create_order_order()
    url = reverse("order_order_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_order_update_view():
    product = test_helpers.create_product_product()
    client = test_helpers.create_client_client()
    client = Client()
    instance = test_helpers.create_order_order()
    url = reverse("order_order_update", args=[instance.pk, ])
    data = {
        "product": product.pk,
        "client": client.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_offer_list_view():
    instance1 = test_helpers.create_order_offer()
    instance2 = test_helpers.create_order_offer()
    client = Client()
    url = reverse("order_offer_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_offer_create_view():
    product = test_helpers.create_product_product()
    client = Client()
    url = reverse("order_offer_create")
    data = {
        "new_price": 1,
        "product": product.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_offer_detail_view():
    client = Client()
    instance = test_helpers.create_order_offer()
    url = reverse("order_offer_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_offer_update_view():
    product = test_helpers.create_product_product()
    client = Client()
    instance = test_helpers.create_order_offer()
    url = reverse("order_offer_update", args=[instance.pk, ])
    data = {
        "new_price": 1,
        "product": product.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
