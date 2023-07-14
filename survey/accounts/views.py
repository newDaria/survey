
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm




def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('index')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('login')


    else:
        return render(request, 'accounts/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('index')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


# from django.urls import reverse_lazy
# from django.views.generic import CreateView
#
# from . import forms
#
# # Create your views here.
# class SignUp(CreateView):
#     form_class = forms.UserCreationForm
#     # перенаправлять только когда будет нажата submit button
#     success_url = reverse_lazy('login')
#     # указывает на шаблон HTML, который будет использоваться для отображения страницы регистрации.
#     template_name = 'accounts/signup.html'
#
