from .models import cart


def cart_context_processors(request):
    cartid = request.session.get("cart_id")
    count = None
    if cartid is not None:
        cart_id = cart.objects.get(id = cartid)
        count = cart.cartitem_set.all().count()
    

    return{}