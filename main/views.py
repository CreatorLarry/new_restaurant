from random import choice

from django.shortcuts import render, redirect

from django.contrib import messages

from main.models import Dish, Reservation, Order


# Create your views here.
def home(request):
    dishes = Dish.objects.all()
    return render(request, 'home.html', {'dishes': dishes})


def about(request):
    return render(request, 'about.html')


def book_table(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        guest = request.POST.get("people")
        message = request.POST.get("message")

        if not name or not email or not phone or not date or not time or not guest:
            messages.error(request, "Please fill all fields")
            return redirect("book-table")

        book_table = Reservation.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            guest=guest,
            message=message,
            status="pending"
        )
        messages.success(
            request, "Your table booking request has been successfully placed! We will call back and send an email to confirm your booking"
        )
    return render(request, 'book-table.html')


def menu(request):
    categories = Dish.objects.values_list('category', flat=True).distinct()
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {'dishes': dishes, 'categories': categories})


def order(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        food_item = request.POST.get("food_item")
        quantity = request.POST.get("quantity")
        delivery_address = request.POST.get("delivery_address")
        message = request.POST.get("message")

        if not name or not email or not phone or not food_item or not quantity or not delivery_address:
            messages.error(request, "All fields are required!")
            return redirect("order")

        order = Order.objects.create(
            name=name,
            email=email,
            phone=phone,
            food_item=food_item,
            quantity=quantity,
            delivery_address=delivery_address,
            message=message,
        )
        order.save()
        messages.success(request,
                         'Your order has been placed successfully!. We will call back and send an email to confirm your order.')

        return redirect('order')

    return render(request, 'order.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')
