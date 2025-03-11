from django import forms
from .models import Dish, Reservation


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'image', 'category']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name','phone','email', 'date', 'time', 'guest', 'message']