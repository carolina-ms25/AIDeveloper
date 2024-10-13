from django import forms
class CasaForm(forms.Form):
    antiguedad = forms.IntegerField(label='Antigüedad',min_value=1)
    nro_pisos = forms.IntegerField(label='Número de pisos', min_value=1)    
    dormitorios = forms.IntegerField(label='Dormitorios',min_value=1)
    area_constr_m2 = forms.IntegerField(label='Área construida en m2',min_value=1)
    area_total_m2 = forms.IntegerField(label='Área total en m2',min_value=1)
