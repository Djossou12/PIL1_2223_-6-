"""
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # ...
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
"""

from django.shortcuts import render, redirect
# from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Licence1IA

def check_existing_user(username, email):
    existing_user = User.objects.filter(username=username) | User.objects.filter(email=email)
    
    if existing_user.exists():
        return True 
    else:
        return False  


def log(request):
    if request.user.is_authenticated:
        return redirect('eduapp:index')
    else:  
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username= username , password = password)

            if user is not None :
                login(request,user)
                return redirect('eduapp:index')
            else:
                messages.info(request,'Le nom utilisateur ou le mot de passe est incorrect ')

    context={}
    return render(request, 'eduapp/login.html', context)

def logoutUser (request):
    logout(request)
    return redirect('eduapp:login')

def signup(request):
    if request.user.is_authenticated:
        return redirect('eduapp:index')
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
                    messages.success(request,'Page d\'inscription créée avec succès ')
                    return redirect('eduapp:index')
                    
        else:
            form = SignupForm()  
    context={'form':form, 'messages': messages.get_messages(request)}
    
    return render(request, 'eduapp/signup.html', context)


@login_required(login_url='eduapp:login')
def index(request):
    # if Licence1IA.Jours == "lundi":
        # context = {"books": Licence1IA.objects.all(),"a":Licence1IA.Jours}
    # else:
    context={}
    context["books"] = Licence1IA.objects.all()
    return render(request, 'eduapp/index.html', context)




