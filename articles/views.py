from django.shortcuts import render

from articles.models import Article

# Create your views here.
def article_detail_view(request, id=None):
    if id is None:
        article_obj = None
    else:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    
    return render(request, "articles/detail.html", context=context)