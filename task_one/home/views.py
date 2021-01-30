from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .forms import productForm
from django.urls import reverse
from .models import product
# Create your views here.

class HomeView(generic.ListView):
    queryset = product.objects.filter(Activate=True).order_by("-id")
    template_name = "home/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "Product View"
        print(context)
        return context

class CreateProjectView(SuccessMessageMixin,generic.CreateView):
    form_class = productForm
    template_name = 'home/create.html'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Product add successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Add Product"
        return context


class ProductUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = productForm
    template_name = 'home/create.html'
    queryset = product.objects.all()

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Product update successfully."

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Edit Product"
        return context


class ProductSoftleteView(SuccessMessageMixin,generic.View):
    def get_success_message(self, cleaned_data):
        return "Product remove successfully."

    def get(self, request, *args, **kwargs):
        prodict_id = self.kwargs.get("prodict_id")
        product.objects.filter(id=prodict_id).update(Activate=False)
        return HttpResponseRedirect(reverse('home:ViewProduct'))