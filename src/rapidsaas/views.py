import pathlib
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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


VALID_CODE = 'authorized-user'


def password_protected_view(request, *args, **kwargs):
    """
    View for restricted access/protected pages
    """
    is_allowed = request.session.get('protected-page-allowed') or 0
    if request.method == 'POST':
        # 'code' from input name in protected/entry.html form
        user_password_data = request.POST.get('code') or None
        if user_password_data == VALID_CODE:
            # set authenticated to True
            is_allowed = 1
            request.session['protected-page-allowed'] = is_allowed
    if is_allowed:
        return render(request, 'protected/success.html', {})
    return render(request, 'protected/authenticate.html', {})


@login_required
def login_required_view(request):
    return render(request, 'protected/user-only.html')


@staff_member_required
def staff_only_view(request):
    return render(request, 'protected/user-only.html')
