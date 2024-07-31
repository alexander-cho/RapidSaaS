import pathlib
from django.http import HttpResponse
from django.shortcuts import render

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    # path = this_dir / 'home.html'
    # html_ = path.read_text()
    my_title = 'RapidSaaS Prototype'
    context = {
        'my_title': my_title
    }
    html_template = 'home.html'
    return render(request, html_template, context)


def old_home_page_view(request, *args, **kwargs):
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
