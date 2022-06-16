from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("type", api.typeViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("type/type/", views.typeListView.as_view(), name="type_type_list"),
    path("type/type/create/", views.typeCreateView.as_view(), name="type_type_create"),
    path("type/type/detail/<int:pk>/", views.typeDetailView.as_view(), name="type_type_detail"),
    path("type/type/update/<int:pk>/", views.typeUpdateView.as_view(), name="type_type_update"),
    path("type/type/delete/<int:pk>/", views.typeDeleteView.as_view(), name="type_type_delete"),
)
