from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from articles.models import Article
from articles.forms import ArticleForm


# Create your views here.
def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")     # input name defined in base.html

    if query is not None:
        article_obj = Article.objects.get(id=query)
    else:
        article_obj = None

    context = {
        "object": article_obj
    }

    return render(request, "articles/search.html", context=context)


@login_required
def article_create_view(request):
    form = ArticleForm()
    context = {"article_form": form}
    if request.method == "POST":
        form = ArticleForm(request.POST)
        context["article_form"] = form

        if form.is_valid():
            new_article = form.save()
            context["new_article"] = new_article
            context["created"] = True

    return render(request, "articles/create.html", context=context)


def article_detail_view(request, id=None):
    if id is None:
        article_obj = None
    else:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }

    return render(request, "articles/detail.html", context=context)
