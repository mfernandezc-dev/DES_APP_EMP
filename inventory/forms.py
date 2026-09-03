from django import forms


class ProductoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label='Nombre del producto'
    )

    categoria = forms.CharField(
        max_length=50,
        label='Categoría'
    )

    precio = forms.FloatField(
        label='Precio (S/)',
        min_value=0.01
    )

    stock = forms.IntegerField(
        label='Cantidad en stock',
        min_value=0
    )