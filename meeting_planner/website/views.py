from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("This page was served at {}".format(str(datetime.now())))


def about(request):
    return HttpResponse("Myself Rohit Munda and I am a Data Science Consultant.")
