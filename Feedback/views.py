from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib import sessions

from Feedback.forms import FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

class FeedbackFormView(FormView):
    template_name = "Feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/feedback/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = "Feedback/success.html"


