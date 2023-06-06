from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
def index(request):
    return render(request, "blog/index.html", {})


def cats(request, pageid):
    if request.GET:
        print(request.GET['name'])
        print(request.GET['name'])
    if int(pageid) == 100:
        raise Http404
    if int(pageid) == 50:
        return redirect('home')

    return redirect(request, 'blog/views_user.html', {})


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страниц д1а ца хутт</h1>")
