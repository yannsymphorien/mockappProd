from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("order", api.orderViewSet)
router.register("offer", api.offerViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("order/order/", views.orderListView.as_view(), name="order_order_list"),
    path("order/order/create/", views.orderCreateView.as_view(), name="order_order_create"),
    path("order/order/detail/<int:pk>/", views.orderDetailView.as_view(), name="order_order_detail"),
    path("order/order/update/<int:pk>/", views.orderUpdateView.as_view(), name="order_order_update"),
    path("order/order/delete/<int:pk>/", views.orderDeleteView.as_view(), name="order_order_delete"),
    path("order/offer/", views.offerListView.as_view(), name="order_offer_list"),
    path("order/offer/create/", views.offerCreateView.as_view(), name="order_offer_create"),
    path("order/offer/detail/<int:pk>/", views.offerDetailView.as_view(), name="order_offer_detail"),
    path("order/offer/update/<int:pk>/", views.offerUpdateView.as_view(), name="order_offer_update"),
    path("order/offer/delete/<int:pk>/", views.offerDeleteView.as_view(), name="order_offer_delete"),
)
