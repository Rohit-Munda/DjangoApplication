from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Meeting, Room


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/details.html", {"meeting": meeting})


def rooms(request):
    return render(request, "meetings/room_details.html", {"rooms": Room.objects.all()})


ModelForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == "POST":
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = ModelForm()
    return render(request, "meetings/new.html", {"form": form})