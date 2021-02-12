import wikipedia
from django import views
# Create your views here.
from django.shortcuts import render

from movies.forms import WikiForm


class WikipediaView(views.generic.View):
    form_class = WikiForm

    def get(self, request, *args, **kwargs):
        return render(request, 'wiki.html', context={'form': WikiForm()})

    def post(self, request, *args, **kwargs):
        query = request.POST
        result = wikipedia.search(query['query'])

        return render(request, 'wiki.html', context={'results': result, 'form': WikiForm()})
