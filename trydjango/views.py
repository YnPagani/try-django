"""
To render html views
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

def home_view(request):
    rand_id = random.randint(1, 4)
    article_obj = Article.objects.get(id=rand_id)
    article_query_set = Article.objects.all()
    
    context = {
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id,
        "article_list": article_query_set
    }
    
    html_str = render_to_string("home_view.html", context=context)
    return HttpResponse(html_str)