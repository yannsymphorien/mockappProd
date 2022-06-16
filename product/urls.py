from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("product", api.productViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("product/product/", views.productListView.as_view(), name="product_product_list"),
    path("product/product/create/", views.productCreateView.as_view(), name="product_product_create"),
    path("product/product/detail/<int:pk>/", views.productDetailView.as_view(), name="product_product_detail"),
    path("product/product/update/<int:pk>/", views.productUpdateView.as_view(), name="product_product_update"),
    path("product/product/delete/<int:pk>/", views.productDeleteView.as_view(), name="product_product_delete"),
)
