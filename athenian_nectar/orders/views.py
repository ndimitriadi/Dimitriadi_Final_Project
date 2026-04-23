from django.shortcuts import render, redirect, get_object_or_404
from experiences.models import Experience
from .models import Order, OrderItem

def add_to_cart(request, exp_id):
    if request.method == 'POST':
        experience = get_object_or_404(Experience, id=exp_id)
        
        booking_date = request.POST.get('booking_date')
        quantity = int(request.POST.get('quantity', 1))
        
        cart = request.session.get('cart', {})
        
        #this key combines the id with the date, so the item appears as one
        item_key = f"{exp_id}_{booking_date}"

        if item_key in cart:
            cart[item_key]['quantity'] += quantity
        else:
            cart[item_key] = {
                'exp_id': exp_id,
                'price': float(experience.price),
                'quantity': quantity,
                'date': booking_date
            }

        request.session['cart'] = cart
        return redirect('cart_detail')
        
    return redirect('experience_detail', exp_id=exp_id)

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0

    for item_key, item_data in cart.items():
        try:
            experience = Experience.objects.get(id=int(item_data['exp_id']))
            total_price = item_data['price'] * item_data['quantity']
            cart_total += total_price
            
            cart_items.append({
                'item_key': item_key,
                'experience': experience,
                'quantity': item_data['quantity'],
                'date': item_data['date'],
                'total_price': total_price
            })
        except Experience.DoesNotExist:
            continue

    context = {'cart_items': cart_items, 'cart_total': cart_total}
    return render(request, 'orders/cart.html', context)


def update_cart(request, item_key):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        new_date = request.POST.get('booking_date')
        
        cart = request.session.get('cart', {})

        if item_key in cart:
            if quantity > 0:
                old_item_data = cart[item_key]
                exp_id = old_item_data['exp_id']

                if new_date and new_date != old_item_data['date']:
                    
                    new_item_key = f"{exp_id}_{new_date}"
                    
                    #combining guests if they changed the date to the same as another order
                    if new_item_key in cart:
                        cart[new_item_key]['quantity'] += quantity
                    else:
                        cart[new_item_key] = {
                            'exp_id': exp_id,
                            'price': old_item_data['price'],
                            'quantity': quantity,
                            'date': new_date
                        }
                    
                    del cart[item_key]
                
                else:
                    cart[item_key]['quantity'] = quantity
            else:
                del cart[item_key]

        request.session['cart'] = cart
        
    return redirect('cart_detail')


def remove_from_cart(request, item_key):
    cart = request.session.get('cart', {})
    if item_key in cart:
        del cart[item_key]
        request.session['cart'] = cart
    return redirect('cart_detail')


def checkout(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart_detail')

        cart_total = sum(item_data['price'] * item_data['quantity'] for item_data in cart.values())

        order = Order.objects.create(user=request.user, total_price=cart_total)

        for item_key, item_data in cart.items():
            experience = Experience.objects.get(id=int(item_data['exp_id']))
            OrderItem.objects.create(
                order=order,
                experience=experience,
                price=item_data['price'],
                quantity=item_data['quantity'],
                booking_date=item_data['date']
            )

        request.session['cart'] = {}
        return redirect('dashboard')
        
    return redirect('cart_detail')