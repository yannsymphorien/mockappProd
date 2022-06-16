from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class orderListView(generic.ListView):
    model = models.order
    form_class = forms.orderForm


class orderCreateView(generic.CreateView):
    model = models.order
    form_class = forms.orderForm


class orderDetailView(generic.DetailView):
    model = models.order
    form_class = forms.orderForm


class orderUpdateView(generic.UpdateView):
    model = models.order
    form_class = forms.orderForm
    pk_url_kwarg = "pk"


class orderDeleteView(generic.DeleteView):
    model = models.order
    success_url = reverse_lazy("order_order_list")


class offerListView(generic.ListView):
    model = models.offer
    form_class = forms.offerForm


class offerCreateView(generic.CreateView):
    model = models.offer
    form_class = forms.offerForm


class offerDetailView(generic.DetailView):
    model = models.offer
    form_class = forms.offerForm


class offerUpdateView(generic.UpdateView):
    model = models.offer
    form_class = forms.offerForm
    pk_url_kwarg = "pk"


class offerDeleteView(generic.DeleteView):
    model = models.offer
    success_url = reverse_lazy("order_offer_list")
