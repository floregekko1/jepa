from django.shortcuts import render
from datetime import datetime
from jepa.models import Article
from django.http import Http404
from django.views import View
from django.views.generic import TemplateView 
from .models import Article


def date_actuelle(request):
	return render(request, 'jepa/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
	total = nombre1 + nombre2
	return render(request, 'jepa/addition.html', context_instance=RequestContext(request))


def base(request):
	return render(request, 'jepa/base.html', locals())

def index(request):
	return render(request, 'jepa/index.html', locals())

def accueil(request):
	queryset=Article.objects.all()
	context = {
		"objet_list": queryset	
	}
	return render(request, 'jepa/accueil.html', context)


def nousconnaitre(request):
	return render(request, 'jepa/nousconnaitre.html', locals())

def archive(request):
	return render(request, 'jepa/archive.html', locals())

def dons(request):
	return render(request, 'jepa/dons.html', locals())
def contact(request):
	return render(request, 'jepa/contact.html', locals())
def chat(request):
	return render(request, 'jepa/chat.html', locals())
def blog(request):
	return render(request, 'jepa/blog.html', locals())

def lire(request,id):
# Affiche le texte complet
	try:
		article = Article.objects.get(id=id)
	except Article.DoesNotExist:
		raise Http404
	return render(request,'jepa/lire.html', {'article':article})



def faltpage(request,id):
# Affiche le texte complet
	try:
		article = FaltPageAdmin.objects.get(id=id)
	except FaltPageAdmin.DoesNotExist:
		raise Http404
	return render(request,'jepa/accueil/', {'article':article})


















