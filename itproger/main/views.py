from django.http import HttpResponse
from django.shortcuts import render
from .models import MyModel


def index(request):
    users = MyModel.objects.all()
    return render(request, "chat.html", {'users': users})


def showcookie(request):
    show = request.COOKIES.get('CookieName')
    if show:
        html = "Hello! {0}".format(show)
    else:
        html = "Cookie 'cookieName' is not set."
    return HttpResponse(html)


def setcookie(request):
    html = HttpResponse("<h1>Hello</h1>")
    html.set_cookie('CookieName',
                    'Hello this is your Cookies',
                    max_age=None)
    return html
