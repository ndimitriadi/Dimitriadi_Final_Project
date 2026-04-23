def cart_processor(request):
    cart = request.session.get('cart', {})
    cart_item_count = sum(item['quantity'] for item in cart.values())
    
    return {'cart_item_count': cart_item_count}