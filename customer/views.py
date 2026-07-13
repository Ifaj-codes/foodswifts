from django.shortcuts import render, redirect
from .models import MenuItem, OrderModel

def index(request):
    return render(request, 'customer/index.html')
def menu(request):
    if request.method == 'POST':
        ids = request.POST.getlist('items[]')
        total = 0
        order = OrderModel.objects.create(price=0)
        for i in ids:
            food = MenuItem.objects.get(id=i)
            total += food.price
            order.items.add(food)
        order.price = total
        order.save()
        
        
        return render(request, 'customer/payment.html', {'total': total, 'order_id': order.id})
    
    foods = MenuItem.objects.all()
    return render(request, 'customer/menu.html', {'items': foods})
from django.contrib import messages


def payment_view(request):
    if request.method == 'POST':
        messages.success(request, "Payment Successful! Your order is placed.")
        return redirect('payment') 
    return render(request, 'customer/payment.html')