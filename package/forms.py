from django import forms

class CheckoutForm(forms.Form):
    CHOICES= [('car', 'van', 'temp','bus')]
    choice_field= forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)