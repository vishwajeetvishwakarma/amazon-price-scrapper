from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .form import ProductForm
from .models import Product


def home_page(request):
    discounted = 0
    error = None
    form = ProductForm()
    if request.method == 'POST':
        try:
            form = ProductForm(request.POST or None)
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Opp's couldn't find name and price of this item."
        except:
            error = "Opp's, Something went wrong."
    qs = Product.objects.all()
    qs_count = qs.count()
    for i in qs:
        if i.price_diff != 0:
            discounted += 1
    context = {
        "qs_count": qs_count,
        "qs": qs,
        "error": error,
        'discounted': discounted,
        "form": form
    }
    return render(request, "home.html", context)


class ProductDeleteView(DeleteView):
    template_name = "comfirm_del.html"
    model = Product
    success_url = reverse_lazy('home')

def update_price(request):
    qs = Product.objects.all()
    for i in qs:
        i.save()
    return redirect("home")