from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

jadvallar=[
    {"1":['Dushanba','Monday','Понедельник'],"french":"lundi","italian":"lunedi","roman":"luni","spanish":"lunes","portu":"segunda"},
    {"1":['Seshanba','Thuesday','Вторник'],"french":"lundi","italian":"lunedi","roman":"luni","spanish":"lunes","portu":"segunda"},
    {"1":['Chorshanba','Wednesday','Среда'],"french":"lundi","italian":"lunedi","roman":"luni","spanish":"lunes","portu":"segunda"},
    {"1":['Payshanba','Thursday','Четверг'],"french":"lundi","italian":"lunedi","roman":"luni","spanish":"lunes","portu":"segunda"},
    {"1":['Juma','Friday','Пятница'],"french":"lundi","italian":"lunedi","roman":"luni","spanish":"lunes","portu":"segunda"},
    {"1":['shanba','Saturday','Суббота'],"french":"lundi","italian":"lunedi","roman":"luni","spanish":"lunes","portu":"segunda"},
    {"1":['Yakshanba','Sunday','Воскресенье'],"french":"lundi","italian":"lunedi","roman":"luni","spanish":"lunes","portu":"segunda"}

]
def week(request):
   return render(request,'week.html',context={'jadvallar':jadvallar})


def week_uz(request):
    return render(request,'week_uz.html',context={'jadvallar':jadvallar})



def week_en(request):
    return render(request,'week_en.html',context={'jadvallar':jadvallar})


def week_ru(request):
    return  render(request,'week_ru.html',context={'jadvallar':jadvallar})
