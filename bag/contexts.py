from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    # empty bag for products to go 
    bag_items = []

    # default zero for total cost and product count
    total = 0
    product_count = 0

    # Getting bag it if it already exists or initializing it to an empty dictionary if not
    bag = request.session.get('bag', {})
    
    for item_id, item_data in bag.items():
        # if integer we know its a quantity
        if isinstance(item_data, int):
            # get the product
            product = get_object_or_404(Product, pk=item_id)
            # add its quantity times the price to the total
            total += item_data * product.price
            # increment the product count by the quantity
            product_count += item_data
            #  dictionary containing id, quantity & product object
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        # if not integer, then its in dictionary
        else:
            # iterate through the inner dictionary of items_by_size
            # incrementing the product count and total accordingly.
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                #for each item add the size to the 
                # bag items returned to the template 
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })


    # give free delivery if spend more than amount
    # specified in free delivery threshold in settings.py
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PRECENTAGE / 100)

        # let user know how much more to spend
        # to get free delivery 
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        # If the total is greater than or equal to the threshold
        # set delivery and the free_delivery_delta to zero
        delivery = 0
        free_delivery_delta = 0

    # calculate grand total by adding delivery charge to the total
    grand_total = delivery + total

    context = {
        # everything in this context will be available in every template.
        # In every app across the entire project.
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context