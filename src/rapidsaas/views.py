import pathlib
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from visits.models import PageVisit


this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    # record a page visit 
    PageVisit.objects.create(path=request.path)

    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    # path = this_dir / 'home.html'
    # html_ = path.read_text()
    my_title = 'RapidSaaS Prototype'
    context = {
        'my_title': my_title,
        'page_visit_count': page_qs.count(),
        'total_visit_count': qs.count()
    }
    html_template = 'home.html'

    return render(request, html_template, context)


def about_page_view(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    # record a page visit 
    PageVisit.objects.create(path=request.path)
    
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    # path = this_dir / 'home.html'
    # html_ = path.read_text()
    my_title = 'RapidSaaS Prototype'
    context = { 
        'my_title': my_title,
        'page_visit_count': page_qs.count(),
        'total_visit_count': qs.count()
    }
    html_template = 'home.html'

    return render(request, html_template, context)


def old_home_page_view(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    # path = this_dir / 'home.html'
    # html_ = path.read_text()
    my_title = 'RapidSaaS Prototype'
    context = {
        'my_title': my_title
    }
    html_ = """
            <!DOCTYPE html>
            <html>
                <body>
                    <h1>{my_title}</h1>
                </body>
            </html>
            """.format(**context)
    return HttpResponse(html_)
