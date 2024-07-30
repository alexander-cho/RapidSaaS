import pathlib
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    # path = this_dir / 'home.html'
    # html_ = path.read_text()
    html_ = """
            <!DOCTYPE html>
            <html>
                <body>
                    <h1>In line html</h1>
                </body>
            </html>
            """ 
    return HttpResponse(html_)
