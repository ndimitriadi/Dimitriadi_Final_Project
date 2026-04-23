from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from experiences.models import Experience
from .models import Order, OrderItem

# 1. Add an item to the session cart
def add_to_cart(request, exp_id):
    experience = get_object_or_404(Experience, id=exp_id)
    
    # Grab the cart from the session, or create an empty dictionary
    cart = request.session.get('cart', {})
    exp_id_str = str(exp_id) # Session keys must be strings!

    # If it's already in the cart, add 1 to the quantity
    if exp_id_str in cart:
        cart[exp_id_str]['quantity'] += 1
    # If it's new, add it to the cart with its current price
    else:
        cart[exp_id_str] = {
            'price': float(experience.price),
            'quantity': 1
        }

    # Save the updated cart back into the session
    request.session['cart'] = cart
    messages.success(request, f"{experience.title} added to your cart!")
    
    return redirect('cart_detail')

# 2. View the cart page
def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0

    # Match the session data with real database objects to get images and titles
    for exp_id, item_data in cart.items():
        # Safely fetch the experience
        try:
            experience = Experience.objects.get(id=int(exp_id))
            total_price = item_data['price'] * item_data['quantity']
            cart_total += total_price
            
            cart_items.append({
                'experience': experience,
                'quantity': item_data['quantity'],
                'total_price': total_price
            })
        except Experience.DoesNotExist:
            continue # If an experience was deleted from the database, skip it

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total
    }
    # Notice we changed the folder name to 'orders' here!
    return render(request, 'orders/cart.html', context)

# 3. Securely check out and write to the database
def checkout(request):
    if request.method == 'POST':
        # Must be logged in to buy!
        if not request.user.is_authenticated:
            messages.error(request, "Please log in to complete your purchase.")
            return redirect('login')

        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty.")
            return redirect('cart_detail')

        # 1. Calculate the grand total
        cart_total = sum(Experience.objects.get(id=int(exp_id)).price * item_data['quantity'] for exp_id, item_data in cart.items())

        # 2. Create the main Order (The Receipt)
        order = Order.objects.create(
            user=request.user,
            total_price=cart_total
        )

        # 3. Create the individual Line Items
        for exp_id, item_data in cart.items():
            experience = Experience.objects.get(id=int(exp_id))
            OrderItem.objects.create(
                order=order,
                experience=experience,
                price=experience.price, # Freezes the price at the time of checkout!
                quantity=item_data['quantity']
            )

        # 4. Wipe the session cart clean!
        request.session['cart'] = {}
        messages.success(request, f"Checkout successful! Order #{order.id} confirmed.")
        
        # Send them to the dashboard to see their new order history
        return redirect('dashboard')
        
    return redirect('cart_detail')

# Add these to the bottom of orders/views.py

def update_cart(request, exp_id):
    if request.method == 'POST':
        # Grab the new quantity from the form, default to 1 if something goes wrong
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        exp_id_str = str(exp_id)

        if exp_id_str in cart:
            if quantity > 0:
                cart[exp_id_str]['quantity'] = quantity
                messages.success(request, "Cart updated!")
            else:
                # If they set quantity to 0, just remove it entirely
                del cart[exp_id_str]
                messages.success(request, "Item removed from cart.")

        # Save the updated dictionary back to the session
        request.session['cart'] = cart
        
    return redirect('cart_detail')

def remove_from_cart(request, exp_id):
    cart = request.session.get('cart', {})
    exp_id_str = str(exp_id)

    if exp_id_str in cart:
        del cart[exp_id_str]
        request.session['cart'] = cart
        messages.success(request, "Item removed from cart.")

    return redirect('cart_detail')