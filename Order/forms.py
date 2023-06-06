from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
    first_name = forms.CharField(label="First name", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'First name?', 'id': 'id_first_name'

                }))
    last_name = forms.CharField(label="Last name", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'Second name?', 'id': 'id_last_name'

                }))
    email = forms.EmailField(label="Email", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'Email?', 'id': 'id_email'

                }))
    address = forms.CharField(label="Address", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'address?', 'id': 'id_address'

                }))
    postal_code = forms.CharField(label="Postal code", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'Postal Code?', 'id': 'id_postal_code'

                }))
    city = forms.CharField(label="City", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'City?', 'id': 'id_city'

                }))    