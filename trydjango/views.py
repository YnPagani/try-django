"""
To render html views
"""
from django.http import HttpResponse

def home_view(request):
    html_str = """<h1>Hello Bro</h1>"""
    return HttpResponse(html_str)