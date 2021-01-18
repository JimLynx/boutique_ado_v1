from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    # empty bag for products to go 
    bag_items = []

    # default zero for total cost and product count
    total = 0
    product_count = 0

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