from django import forms

class TeleCodeForm(forms.Form):
    telecode = forms.CharField(label="Input", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'input', 

                }),max_length=4, min_length=4)
    

class TeleidForm(forms.Form):
    teleid = forms.CharField(label="Input", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'input', 

                }),max_length=10, min_length=8)
