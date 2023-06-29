from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from .models import Book
from .models import Book1
from .models import Book2
from .models import Book3
from .models import Book4
from .models import Book5
from .models import Book6
from .models import Book7
from .models import Book8
from .models import Book9
from .models import Book10
from .models import Book11
from .models import Book12
from .models import Book13
from .models import Book14

def check_existing_user(username, email):
    existing_user = User.objects.filter(username=username) | User.objects.filter(email=email)
    
    if existing_user.exists():
        return True 
    else:
        return False  


def log(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:  
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username= username , password = password)

            if user is not None :
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Le nom utilisateur ou le mot de passe est incorrect ')

    context={}
    return render(request, 'eduapp/login.html', context)


def logoutUser (request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                print(username)
                print(email)
                
                if User.objects.filter(username=username).exists():
                    form.add_error('username', 'Cet utilisateur existe déjà veuillez reéssayez.')
                    messages.error(request, 'Cet utilisateur existe déjà.')
                    print("erreur")
                
                if User.objects.filter(email=email).exists():
                    form.add_error('email', 'Cette adresse e-mail est déjà utilisée.')
                    messages.error(request, 'Cette adresse e-mail est déjà utilisée.') 
                    print("erreur2") 
            
                if not form.errors:  
                    form.save()
                    return redirect('index')
                    
        else:
            form = SignupForm()  
    context={'form':form, 'messages': messages.get_messages(request)}
    
    return render(request, 'eduapp/signup.html', context)






@login_required(login_url='login')
def index(request):
    context = {"message": "Hello World !"}
    template = loader.get_template("eduapp/index.html")
    return HttpResponse(template.render(context, request))


def profile(request):
    return render(request,'eduapp/profile.html')

def etudiant(request):
    return render(request,'eduapp/etudiant.html')

def licence1ep(request):
    return render(request,'eduapp/licence1ep.html')

def licence2ep(request):
    return render(request,'eduapp/licence2ep.html')

def licence3ep(request):
    return render(request,'eduapp/licence3ep.html')

def massehoraire1(request):
    return render(request,'eduapp/massehoraire1.html')

def massehoraire2(request):
    return render(request,'eduapp/massehoraire2.html')

def massehoraire3(request):
    return render(request,'eduapp/massehoraire3.html')

def IA_1(request):
    context = {"books": Book.objects.all()}
    return render(request,'eduapp/IA_1.html',context)

def IA_2(request):
    context = {"books": Book1.objects.all()}
    return render(request,'eduapp/IA_2.html',context)

def IA_3(request):
    context = {"books": Book2.objects.all()}
    return render(request,'eduapp/IA_3.html',context)

def IM_1(request):
    context = {"books": Book3.objects.all()}
    return render(request,'eduapp/IM_1.html',context)

def IM_2(request):
    context = {"books": Book4.objects.all()}
    return render(request,'eduapp/IM_2.html',context)

def IM_3(request):
    context = {"books": Book5.objects.all()}
    return render(request,'eduapp/IM_3.html',context)

def GL_1(request):
     context = {"books": Book6.objects.all()}
     return render(request,'eduapp/GL_1.html',context)

def GL_2(request):
    context = {"books": Book7.objects.all()}
    return render(request,'eduapp/GL_2.html',context)

def GL_3(request):
    context = {"books": Book8.objects.all()}
    return render(request,'eduapp/GL_3.html',context)

def SEIoT1(request):
    context = {"books": Book9.objects.all()}
    return render(request,'eduapp/SE&IoT_1.html',context)

def SEIoT2(request):
    context = {"books": Book10.objects.all()}
    return render(request,'eduapp/SE&IoT_2.html',context)

def SEIoT3(request):
    context = {"books": Book11.objects.all()}
    return render(request,'eduapp/SE&IoT_3.html',context)

def SI_1(request):
    context = {"books": Book12.objects.all()}
    return render(request,'eduapp/SI_1.html',context)

def SI_2(request):
    context = {"books": Book13.objects.all()}
    return render(request,'eduapp/SI_2.html',context)

def SI_3(request):
    context = {"books": Book14.objects.all()}
    return render(request,'eduapp/SI_3.html',context)



