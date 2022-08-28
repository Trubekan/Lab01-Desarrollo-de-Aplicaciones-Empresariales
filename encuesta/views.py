from django.http import HttpResponse

def index(request):
    return HttpResponse("Desde la vista de encuestas!")

def detalle(request, pregunta_id):
    return HttpResponse("Estas viendo la pregunta %s." % pregunta_id)

def resultados(request, pregunta_id):
    response = "Estas viendo los resultado de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def votar(request, pregunta_id):
    return HttpResponse("Estas votando por la pregunta %s." % pregunta_id)

def suma(request,a,b):
    resultado= a+b
    return HttpResponse("La suma de  %s + %s = %s" % (a,b,resultado))

def resta(request,a,b):
    resultado= a-b
    return HttpResponse("La resta de  %s - %s = %s" % (a,b,resultado) )

def multiplicacion(request,a,b):
    resultado= a*b
    return HttpResponse("La multiplicacion de  %s * %s = %s" % (a,b,resultado) )