# feedback/forms.py

# Removed: from time import sleep
# Removed: from django.core.mail import send_mail
from django import forms
from Feedback.tasks import send_feedback_email_task

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'Email?', 

                }))
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={'class': 'text-field__input',
                'placeholder': 'Ur Question?', 

                })
    )

    def send_email(self):
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )