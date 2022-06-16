from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class typeListView(generic.ListView):
    model = models.type
    form_class = forms.typeForm


class typeCreateView(generic.CreateView):
    model = models.type
    form_class = forms.typeForm


class typeDetailView(generic.DetailView):
    model = models.type
    form_class = forms.typeForm


class typeUpdateView(generic.UpdateView):
    model = models.type
    form_class = forms.typeForm
    pk_url_kwarg = "pk"


class typeDeleteView(generic.DeleteView):
    model = models.type
    success_url = reverse_lazy("type_type_list")
