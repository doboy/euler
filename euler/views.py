from django.http import HttpResponse

def home( request ):
    return render_to_response( 'base.html', locals() )
