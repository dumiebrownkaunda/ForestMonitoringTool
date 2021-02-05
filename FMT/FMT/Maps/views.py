from django.shortcuts import render
import requests


# Create your views here.
def imagery_data(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'imagery_data.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyAl7xyUeeED7jmbNIyODPQcd0rH01Sxw4w'  # Don't do this! This is just an example. Secure your keys properly.
    })
