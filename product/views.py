from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class productListView(generic.ListView):
    model = models.product
    form_class = forms.productForm


class productCreateView(generic.CreateView):
    model = models.product
    form_class = forms.productForm


class productDetailView(generic.DetailView):
    model = models.product
    form_class = forms.productForm


class productUpdateView(generic.UpdateView):
    model = models.product
    form_class = forms.productForm
    pk_url_kwarg = "pk"


class productDeleteView(generic.DeleteView):
    model = models.product
    success_url = reverse_lazy("product_product_list")
