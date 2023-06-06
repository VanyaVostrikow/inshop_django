from django import forms
from Feedback.tasks import send_feedback_email_task

class GameForm(forms.Form):
    input = forms.CharField(label="Input", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'input', 'id':'input-field',

                }),max_length=4, min_length=4)
