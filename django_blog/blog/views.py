from django.http import response
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, UserProfileForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
   
@login_required
def homepageview(request):
    return render(request, 'blog/home.html')
    
def registerview(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user=user)
            return redirect('home')
    form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form}) 

class LoginView(FormView):
    template_name = 'blog/login.html'
    form_class = LoginForm
    success_url = 'home'

    def form_valid(self, form):
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            print(user)
            if user is None:
                raise form.ValidationError('Incorrect email or password!')
            login(self.request, user=user)
            print('logged user in')
            return super().form_valid(form)
        
@login_required
def profileview(request):
    id = request.user.id
    user = User.objects.get(id=id)
    print(user)
    if user:
        return render(request, 'blog/profile.html', {'user': user})
    
@login_required
def updateprofile(request):
    id = request.user.id
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = User.objects.get(id=id)
            if user:
                user.username = username
                user.email = email
                user.save()
                print("User updated to:", username, email)
                return redirect('profile')
    form = UserProfileForm()
    return render(request, 'blog/updateprofile.html', {'form': form})


def logoutview(request):
    logout(request)
    return redirect('login')