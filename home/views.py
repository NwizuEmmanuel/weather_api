from django.shortcuts import render
from . import weather_api as w_api

# Create your views here.
def home(request):
    context = None
    if request.method == 'POST':
        location = request.form["weather_location"]
        context = w_api.get_weather_api(location)
        return render(request, "home/index.html", context)
    return render(request, "home/index.html", context)