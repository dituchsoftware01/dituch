from django.shortcuts import render,redirect
from .forms import UserForm
from .models import UserFormData
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.

def home(request):
    return render(request, "index.html")

def form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            mobile = form.cleaned_data["mobile"]
            gender = form.cleaned_data["gender"]
            qualification = form.cleaned_data["qualification"]
            batch = form.cleaned_data["batch"]
            college = form.cleaned_data["college"]
            city = form.cleaned_data["city"]

            try:
                UserFormData(name = name, email = email, mobile = mobile, gender = gender, qualification = qualification,batch = batch, college = college, city = city).save()
            except IntegrityError:
                messages.warning(request,"Hey there! 🌟 Your Mobile or Email already registered!")
            else:
                return redirect("/")
        else:
            # Form is not valid, render it with errors
            return render(request, 'form.html', {'form': form})
    else:
        # If it's a GET request, just render the form
        form = UserForm()
    return render(request, 'form.html', {'form': form})
