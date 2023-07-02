from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from .models import IA_1
from .models import IA_2
from .models import IA_3
from .models import IM_1
from .models import IM_2
from .models import IM_3
from .models import SEIOT_1
from .models import SEIOT_2
from .models import SEIOT_3
from .models import SI_1
from .models import SI_2
from .models import SI_3
from .models import GL_1
from .models import GL_2
from .models import GL_3

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
    if request.user.is_superuser:
        a=True
        context = {"a": a}
    else :
        context={}
    
    return render(request, 'eduapp/index.html', context)



def profile(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a}
    else :
        context={}
    return render(request,'eduapp/profile.html',context)

def etudiant(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a}
    else :
        context={}
    return render(request,'eduapp/etudiant.html',context)

def licence1ep(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a}
    else :
        context={}
    return render(request,'eduapp/licence1ep.html',context)

def licence2ep(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a}
    else :
        context={}
    return render(request,'eduapp/licence2ep.html',context)

def licence3ep(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a}
    else :
        context={}
    return render(request,'eduapp/licence3ep.html',context)

def massehoraire1(request):
    return render(request,'eduapp/massehoraire1.html')

def massehoraire2(request):
    return render(request,'eduapp/massehoraire2.html')

def massehoraire3(request):
    return render(request,'eduapp/massehoraire3.html')

def IA1(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": IA_1.objects.all()}
    else :
        context = {"filieres": IA_1.objects.all()}
    return render(request,'eduapp/IA_1.html',context)

def IA2(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": IA_2.objects.all()}
    else :
        context = {"filieres": IA_2.objects.all()}
    return render(request,'eduapp/IA_2.html',context)

def IA3(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": IA_3.objects.all()}
    else :
        context = {"filieres": IA_3.objects.all()}
    return render(request,'eduapp/IA_3.html',context)

def IM1(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": IM_1.objects.all()}
    else :
        context = {"filieres": IM_1.objects.all()}
    return render(request,'eduapp/IM_1.html',context)

def IM2(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres":IM_2.objects.all()}
    else :
        context = {"filieres": IM_2.objects.all()}
    return render(request,'eduapp/IM_2.html',context)

def IM3(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": IM_3.objects.all()}
    else :
        context = {"filieres": IM_3.objects.all()}
    return render(request,'eduapp/IM_3.html',context)

def GL1(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": GL_1.objects.all()}
    else :
        context = {"filieres": GL_1.objects.all()}
    return render(request,'eduapp/GL_1.html',context)

def GL2(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": GL_2.objects.all()}
    else :
        context = {"filieres": GL_2.objects.all()}
    return render(request,'eduapp/GL_2.html',context)

def GL3(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": GL_3.objects.all()}
    else :
        context = {"filieres": GL_3.objects.all()}
    return render(request,'eduapp/GL_3.html',context)

def SEIoT1(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": SEIOT_1.objects.all()}
    else :
        context = {"filieres": SEIOT_1.objects.all()}
    return render(request,'eduapp/SE&IoT_1.html',context)

def SEIoT2(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": SEIOT_2.objects.all()}
    else :
        context = {"filieres": SEIOT_2.objects.all()}
    return render(request,'eduapp/SE&IoT_2.html',context)

def SEIoT3(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": SEIOT_3.objects.all()}
    else :
         context = {"filieres": SEIOT_3.objects.all()}
    return render(request,'eduapp/SE&IoT_3.html',context)

def SI1(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": SI_1.objects.all()}
    else :
        context = {"filieres": SI_1.objects.all()}
    return render(request,'eduapp/SI_1.html',context)

def SI2(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": SI_2.objects.all()}
    else :
        context = {"filieres": SI_2.objects.all()}
    return render(request,'eduapp/SI_2.html',context)

def SI3(request):
    if request.user.is_superuser:
        a=True
        context = {"a": a,"filieres": SI_3.objects.all()}
    else :
        context = {"filieres": SI_3.objects.all()}
    return render(request,'eduapp/SI_3.html',context)






