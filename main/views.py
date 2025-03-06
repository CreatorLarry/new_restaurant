from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def book_table(request):
    return render(request, 'book-table.html')


def menu(request):
    return render(request, 'menu.html')