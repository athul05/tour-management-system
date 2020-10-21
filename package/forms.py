from django import forms

PKGS= (
    ('Car','Car'),
    ('Mini-Van', 'Mini-Van'),
    ('Traveller', 'Traveller'),
    ('Air-Bus','Air-Bus')
)

RATE= (
    ('1','1 Star'),
    ('2', '2 Star'),
    ('3', '3 Star'),
    ('4', '4 Star'),
    ('5', '5 Star')
)

class CheckoutForm(forms.Form):
    name= forms.CharField(required=True)
    number = forms.CharField(required=True)
    package= forms.ChoiceField(widget=forms.RadioSelect, choices=PKGS, required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),required=True)

class Enquiry(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Name'
    }))
    number = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder':'Phone Number'
    }))
    message= forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Notes'
    }))

class Feed(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Name'
    }))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'E-mail'
    }))
    subject =forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder':'Subject'
    }))

    message = forms.CharField(required=True,widget=forms.Textarea(attrs={
        'placeholder': 'Feedback'
    }))
    rating = forms.CharField( widget = forms.Select(choices=RATE))




