from ssl import HAS_TLSv1_1
from django.http import HttpResponse
from django.shortcuts import render
from admins.models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request,'bands/hello.html',{'bands':bands})

def about(request):
    return HttpResponse('<h1>A propos</h1> <p> nous adorons</p> <header class="de"> <div class="titl"><h1>ODISHOP</h1>pour vos acessoires</div><nav class="nav"><ul><li><a href="Accueil.html" class="acc">Accueil</a></li><li><a href="article.html" class="art">Catalogue</a></li><li><a href="Connexion.html" class="con">Se connecter</a></li></ul></nav></header>')
def text (request):
    return HttpResponse('<div class="aire1"><section id="con">  <h1>ODISHOP</h1><form action="contact">    <div class="oup">      <label for="name"></label>  <input type="text" placeholder="Entrer votre nom ou votre email" required/></div><div class="oup"> <label for="pasword"></label><input type="pasword" name="mot de passe" placeholder="Entrer le mot de passe" required/></div><div style="padding-left: 275px;"> <a href="">Mot de passe oublier?</a> </div><div classe="oup"> <button type="submit">Se connecter</button></div></form><div id="fot"> Vous navaez pas de compte? <a href="">Inscrivez-vous</a> </div></section> </div>')

def user(request):
    return render(request,'listings/user.html',{})
