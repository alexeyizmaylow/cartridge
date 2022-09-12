from django.shortcuts import render, redirect
from .models import *
from .forms import AuthorForm, OrderFormset
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView


def get_test(request):
    if request.method == "GET":
        form = AuthorForm()
        formset = OrderFormset()
        return render(request, 'main/order_cart.html', {'form': form, 'formset': formset})
    elif request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            formset = OrderFormset(request.POST, instance=author)
            if formset.is_valid():
                formset.save()
                return redirect('success/')
        else:
            return render(request, 'main/order_cart.html', {'form': form})


class CartAddView(TemplateView):
    template_name = "main/order_cart.html"

    def get(self, *args, **kwargs):
        form = AuthorForm()
        formset = OrderFormset()
        return self.render_to_response({'form': form, 'formset': formset})

    def post(self, *args, **kwargs):
        form = AuthorForm(data=self.request.POST)
        if form.is_valid():
            author = form.save()
            formset = OrderFormset(data=self.request.POST, instance=author)
            if formset.is_valid():
                formset.save()
                return redirect("success/")
        return self.render_to_response({'form': form, 'formset': formset})


def success(request):
    return render(request, 'main/kek.html')