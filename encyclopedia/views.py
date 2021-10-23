from django.shortcuts import render
from django.http import HttpResponseRedirect


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def article(request, name):
    content = util.get_entry(name)
    if (content == None):
        return render(request, "encyclopedia/article.html", {
            "name": f'Стаття з назвою {name} не знайдена',
            "content": ""
        })
    return render(request, "encyclopedia/article.html", {
        "name": name,
        "content": util.get_entry(name)
    })


def search(request):
    enc_list = []
    if request.method == "POST":
        form = request.POST
        wiki_list = util.list_entries()
        wiki_list_lower = []
        for wiki in wiki_list:
            wiki_list_lower.append(wiki.lower())
        if form['q'].lower() in wiki_list_lower:
            return HttpResponseRedirect(f"/wiki/{form['q']}")
        else:
            for wiki in wiki_list:
                if wiki.lower().find(form['q']) != -1:
                    enc_list.append(wiki)
            return render(request, "encyclopedia/search.html", {
                "entries": enc_list
                })

def add(request):
    return render(request, "encyclopedia/add.html")


