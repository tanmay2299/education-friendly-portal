from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from studentdoubts.models import account, contents


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_superuser:
                auth.login(request,user)
                return redirect('teacher')
            else:
                auth.login(request,user)
                return redirect('new')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request,"login.html")


def new(request):
    return render(request,"new.html")

def home(request):
    return render(request,"login.html")

def logout(request):
    auth.logout(request)    
    return redirect('')

def slotbooking(request):
    return render(request,"slotbooking.html")

def sign(request):
    if request.method=='POST':
        student_name=request.POST['student_name']
        parent_name=request.POST['parent_name']
        phone=request.POST['phone_no']
        subject=request.POST['subject']
        time=request.POST['time']
        d=account(student_name=student_name,parent_name=parent_name,phone=phone,subject=subject,time=time)
        d.save()
        messages.info(request,'Your slot is booked')
        return render(request,'new.html')
    else:
        return render(request,'signup.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Taken')
                return redirect('signup')

            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print('User Created')
            return redirect('login')
        
        else:
            messages.info(request,'Wrong Username or Password')
            return redirect('signup')
        return redirect('/')        
    else:
        return render(request,'signup.html')

def instantsolve(request):
    if request.method=="POST":
        option=request.POST.get('ins')

       # geometry=request.POST.get('geometry')
        if option=="science":
            return render(request,"science.html")
        elif option=="algebra":
            return render(request,"algebra.html")
        else:
            return render(request,"geometry.html")    
    else:
        return render(request,"instantsolve.html")

def videolinks(request):
    if request.method=="POST":
        option=request.POST.get('ins')

       # geometry=request.POST.get('geometry')
        if option=="science":
            return render(request,"videoscience.html")
        elif option=="algebra":
            return render(request,"videoalgebra.html")
        else:
            return render(request,"videogeometry.html")    
    else:
        return render(request,"videolinks.html")


def videoscience(request):
    if request.method=="POST":
        option=request.POST.get('sci')
        objs=contents.objects.filter(subject="Science",topic=option)
        context={'objs':objs}
        return render(request,"videoinfo.html",context)    
    
    else:
        return render(request,"videoscience.html")

def videoalgebra(request):
    if request.method=="POST":
        option=request.POST.get('alg')
        objs=contents.objects.filter(subject="Algebra",topic=option)
        context={'objs':objs}
        return render(request,"videoinfo.html",context)    
    
    else:
        return render(request,"videoalgebra.html")

def videogeometry(request):
    if request.method=="POST":
        option=request.POST.get('geo')
        objs=contents.objects.filter(subject="Geometry",topic=option)
        context={'objs':objs}
        return render(request,"videoinfo.html",context)    
    
    else:
        return render(request,"videogeometry.html")

def science(request):
    if request.method=="POST":
        option=request.POST.get('sci')
        objs=contents.objects.filter(subject="Science",topic=option)
        context={'objs':objs}
        return render(request,"information.html",context)    
    
    else:
        return render(request,"science.html")


def algebra(request):
    if request.method=="POST":
        option=request.POST.get('alg')
        objs=contents.objects.filter(subject="Algebra",topic=option)
        context={'objs':objs}
        return render(request,"information.html",context)    
    
    else:
        return render(request,"algebra.html")
    

def geometry(request):
    if request.method=="POST":
        option=request.POST.get('geo')
        objs=contents.objects.filter(subject="Geometry",topic=option)
        context={'objs':objs}
        return render(request,"information.html",context)    
    
    else:
        return render(request,"geometry.html")


def information(request):
    return render(request,"information.html")

def teacher(request):
    objs=account.objects.all()
    context={'objs':objs}
    return render(request,"teacher.html",context)