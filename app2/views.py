from django.http import HttpResponse

def vista1_app2(request):
    return HttpResponse("<h1>App 2 - Vista 1</h1><p>Contenido principal de la segunda aplicacion.</p><a href='/app2/v2/'>Ir a Vista 2</a>")

def vista2_app2(request):
    return HttpResponse("<h2>App 2 - Vista 2</h2><p>Detalle adicional de la vista.</p><a href='/app2/v1/'>Volver a Vista 1</a>")