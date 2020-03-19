from django.shortcuts import render,redirect

from.forms import *


def home(request):
    return render(request,'myapp/home.html')


def room(request):
    data = Room.objects
    return render(request,'myapp/room.html',{"data":data})


def about(request):
    return render(request,'myapp/about.html')


def room_info(request):
    return render(request,'myapp/room_info.html')


def reserve(request):
    data = Reserve.objects
    form = Reserveform(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request,'myapp/reserve.html',{"form":form})


def reserve_list(request):
    data = Reserve.objects

    return render(request,'myapp/reserve_list.html',{"data":data})



def contact(request):
    return render(request,'myapp/contact.html')