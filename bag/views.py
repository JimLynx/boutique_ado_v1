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

    # set size initial to None
    # if size from form, then qual that
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Check to see if there's a bag variable in the session.
    # & if not, create one
    bag = request.session.get('bag', {})

    if size:
        # If the item is already in the bag 
        if item_id in list(bag.keys()):
            # check if another item of the same id and same size already exists.
            if size in bag[item_id]['items_by_size'].keys():
                # if so increment the quantity for that size and otherwise just set it equal to the quantity
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # but if the item already exists in the bag this is a new size for that item.
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}

    # if there's no size, run this logic
    else:
        if item_id in list(bag.keys()):
            # update quantity of item if it exists in the bag 
            bag[item_id] += quantity
        else:
            # or add to bag if doesn't exist
            bag[item_id] = quantity

    # overwrite variable in session with updated version
    request.session['bag'] = bag

    return render(request, 'bag/bag.html')