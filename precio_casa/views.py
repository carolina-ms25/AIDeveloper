from django.shortcuts import render
from .forms import CasaForm
from .model_regresion import predecir_precio_casa

# Create your views here.
def estimar_precio_casa(request):
    prediccion=None

    if request.method == 'POST':
        form = CasaForm(request.POST)
        if form.is_valid():
            antiguedad = form.cleaned_data['antiguedad']
            nro_pisos = form.cleaned_data['nro_pisos']
            dormitorios = form.cleaned_data['dormitorios']
            area_constr_m2 = form.cleaned_data['area_constr_m2']
            area_total_m2 = form.cleaned_data['area_total_m2']
            prediccion = predecir_precio_casa(antiguedad, nro_pisos, dormitorios, area_constr_m2, area_total_m2)
    else:
        form = CasaForm()
    return render(request, 'precio_casa/estimar_precio_casa.html', {'form': form, 'prediccion': prediccion})

