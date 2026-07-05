from django.shortcuts import render
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
        
        return render(request, 'customer/order_confirmation.html', {'total': total})
        
    foods = MenuItem.objects.all()
    return render(request, 'customer/menu.html', {'items': foods})