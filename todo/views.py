from django.shortcuts import render,redirect
from datetime import datetime
from todo.models import Todo,Reminder,Weather
import requests



# Create your views here.
def dashboard(req):
    todos = Todo.objects.all()
    rem=Reminder.objects.all()
    return render(req,"dashboard.html",{"todos":todos,"rem":rem})
def todo_data(req):
    if req.method=="POST":
        ta=req.POST.get('task')
        da=req.POST.get('date')
        task=Todo(task_name=ta,date=da)
        task.save()
        return redirect(dashboard)
def todo_delete(req,dataid):
    data=Todo.objects.filter(id=dataid)
    data.delete()
    return redirect(dashboard)

def reminder_add(req):
    if req.method == "POST":
        na=req.POST.get('reminderName')
        da=req.POST.get('date')
        ti=req.POST.get('time')
        obj=Reminder(reminder_name=na,date=da,time=ti)
        obj.save()
        return redirect(dashboard)
def reminder_delete(req,dataid):
    data=Reminder.objects.filter(id=dataid)
    data.delete()
    return redirect(dashboard)

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '5146361a6ef5293a8a1829f8c6cda0f0'  # Replace with your API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            city = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']

            weather_data = Weather.objects.create(
                city=city,
                temperature=temperature,
                description=description,
                icon=icon
            )
            weather_data.save()
        else:
            error_message = "City not found!"

    weather = Weather.objects.all().order_by('-id')[:1].first()
    context = {'weather': weather}
    return render(request, 'dashboard.html', context)



