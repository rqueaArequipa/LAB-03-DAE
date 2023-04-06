from django.shortcuts import render
from .models import Opcion, Pregunta

def home(request):
    return render(request, 'main.html')

# Create your views here.
def index(request):
    latest_question_list = Pregunta.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request,'encuesta/index.html',context)

def detalle(request,pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)
    context = {
        'pregunta':pregunta
    }
    
    return render(request,'encuesta/detalle.html',context)

def votar(request,pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)
    opcionSeleccionada = pregunta.opcion_set.get(pk=request.POST['opcion'])
    opcionSeleccionada.votos += 1
    opcionSeleccionada.save()
    context = {
        'pregunta':pregunta
    }
    return render(request,'encuesta/resultados.html',context)

def votos(request):
    pregunta1 = Pregunta.objects.get(pk=1)
    pregunta2 = Pregunta.objects.get(pk=2)
    #opcionSeleccionada = pregunta.opcion_set.get(pk=request.POST['opcion'])
    context = {
        'pregunta1':pregunta1,
        'pregunta2':pregunta2
    }
    return render(request, 'encuesta/votos.html', context)
