#calculates the number of items in cart
def cart_processor(request):
    cart = request.session.get('cart', {})
    cart_item_count = len(cart)
    
    return {'cart_item_count': cart_item_count}