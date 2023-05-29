from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from BankingApp.forms import ApplicationForm
from BankingApp.models import Branch


# Create your views here.

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method =='POST':
        username = request.POST['uname']
        password = request.POST['pwd']
        cpassword = request.POST['cpwd']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name already taken')
                return render(request,"register.html")
            else:
                user = User.objects.create_user(username=username,password=password)

                user.save()
                print("user created")
                messages.info(request, 'account created')
            return render(request,'login.html')

        else:
            messages.info(request,"password not matching")
            print("password not matching")
        return redirect("register")
    return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['uname']
        password=request.POST['pwd']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('sample')
        else:
            messages.info(request,"Invalid credentials")
            return render(request, 'login.html')

    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return  redirect("/")

def application(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accept')
            # messages.success(request,'Application submitted successfully')
        return redirect('/')
    return render(request, 'apln.html', {'form': form})

def cities(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown.html', {'branches': branches})

def sample(request):
    if request.method == 'POST':

       return redirect('application')


    return render(request, 'sample.html')

def accept(request):
    if request.method == 'POST':

       return redirect('/')


    return render(request, 'accept.html')