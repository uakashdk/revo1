from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.


@csrf_exempt
def revo_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not(User.objects.filter(username=username).exists()):
            return redirect('./login')
        else:
            users = authenticate(request, username=username, password=password)
            if users is None:
                return redirect('./login')
            else:
                login(request, users)
                return redirect('./Ambulance')
    return render(request, "login.html")





@csrf_exempt
def revo_index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        emails = request.POST.get('email')

        users = User.objects.filter(username=username)
        if users.exists():
            return redirect('.')
        else:
            user = User.objects.create(
                username=username,
                email = emails
            )
            user.set_password(password)
            user.save()
            return redirect('./Ambulance')


    return render(request, "index.html")


def revo_ambulance(request):
    return render(request, "Ambulance.html")


def revo_ambulanceform(request):
    return render(request, "AmbulanceForm.html")


def revo_doc(request):
    return render(request, "DoctorBooking.html")


def revo_patient(request):
    return render(request, "Patient.html")


def revo_pay(request):
    return render(request, "Payment.html")


