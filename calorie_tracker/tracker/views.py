from django.shortcuts import render
from .models import FoodEntry

def home(request):
    entries = FoodEntry.objects.all()
    return render(request, "tracker/home.html", {"entries": entries})

def search_food(request):
    # Add search logic here if using an external API
    return render(request, "tracker/search.html")
