from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
     return render(request, 'second.html',{'na':''})
def check(request):
     s=request.POST['search']
     if s=='':
          return render(request, 'second.html', {'na': 'Invalid Place'})

     API_KEY = 'Your api key from https://home.openweathermap.org/'
     BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
     URL = BASE_URL + "q=" + s + "&appid=" + API_KEY
     # HTTP request
     response = requests.get(URL)


     s = [s.center(20, '-') ]
     if response.status_code == 200:
          # getting data in the json format
          data = response.json()
          # getting the main dict block
          main = data['main']
          # getting temperature
          temperature = main['temp']
          # getting the humidity
          humidity = main['humidity']
          # getting the pressure
          pressure = main['pressure']
          # weather report
          report = data['weather']
          s .append('Temperature: ' + str(round(temperature - 273.15, 2)) +'Degree C')
          s.append('Humidity: ' + str(humidity) +'%')
          s.append( 'Pressure: ' + str(pressure))
          s.append( 'Weather Report: ' + str(report[0]['description']))
          s +=[''.center(20, '-')]
          return render(request, 'second.html', {'na': s})

     else:
          s="Error in the HTTP request"
          return render(request, 'second.html', {'na': [s]})
