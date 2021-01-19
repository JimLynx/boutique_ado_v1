from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of specified product to shopping bag """

    # get quantity from form 
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Check to see if there's a bag variable in the session.
    # & if not, create one
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        # update quantity of item if it exists in the bag 
        bag[item_id] += quantity
    else:
        # or add to bag if doesn't exist
        bag[item_id] = quantity

    # overwrite variable in session with updated version
    request.session['bag'] = bag

    return render(request, 'bag/bag.html')