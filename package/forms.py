from django import forms

PKGS= (
    ('Car','Car'),
    ('Mini-Van', 'Mini-Van'),
    ('Traveller', 'Traveller'),
    ('Air-Bus','Air-Bus')
)

class CheckoutForm(forms.Form):
    name= forms.CharField(required=True)
    number = forms.CharField(required=True)
    package= forms.ChoiceField(widget=forms.RadioSelect, choices=PKGS, required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),required=True)