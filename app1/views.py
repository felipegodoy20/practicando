from django.http import HttpResponse

def vista1_app1(request):
    return HttpResponse("<h1>App 1 - Vista 1</h1><p>Contenido principal de la primera aplicacion.</p><a href='/app1/v2/'>Ir a Vista 2</a>")

def vista2_app1(request):
    return HttpResponse("<h2>App 1 - Vista 2</h2><p>Detalle adicional de la vista.</p><a href='/app1/v1/'>Volver a Vista 1</a>")