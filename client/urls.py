from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("client", api.clientViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("client/client/", views.clientListView.as_view(), name="client_client_list"),
    path("client/client/create/", views.clientCreateView.as_view(), name="client_client_create"),
    path("client/client/detail/<int:pk>/", views.clientDetailView.as_view(), name="client_client_detail"),
    path("client/client/update/<int:pk>/", views.clientUpdateView.as_view(), name="client_client_update"),
    path("client/client/delete/<int:pk>/", views.clientDeleteView.as_view(), name="client_client_delete"),
)
