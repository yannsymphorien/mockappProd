from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class clientListView(generic.ListView):
    model = models.client
    form_class = forms.clientForm


class clientCreateView(generic.CreateView):
    model = models.client
    form_class = forms.clientForm


class clientDetailView(generic.DetailView):
    model = models.client
    form_class = forms.clientForm


class clientUpdateView(generic.UpdateView):
    model = models.client
    form_class = forms.clientForm
    pk_url_kwarg = "pk"


class clientDeleteView(generic.DeleteView):
    model = models.client
    success_url = reverse_lazy("client_client_list")
