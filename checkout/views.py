from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IBl0kEgnncQ9G2lpSTdOPy6oTMXTEqu5q9JvkhhdRgRB2zp5pBKWEb5E7u6oGvDN9NF3MataGp051S9AdTAtpcf004yicHWWj'
    }
    return render(request, template, context)
