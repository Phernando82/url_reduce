from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from url_reduce.reducer.models import UrlRedirect


def redirecionar(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destino)
