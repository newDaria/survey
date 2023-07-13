from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreationForm
    # перенаправлять только когда будет нажата submit button
    success_url = reverse_lazy('login')
    # указывает на шаблон HTML, который будет использоваться для отображения страницы регистрации.
    template_name = 'accounts/signup.html'

