from django.http import response, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, LoginForm, UserProfileForm, CreatePostForm, UpdatePostForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from datetime import datetime
# Create your views here.
class HomePageView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'all_posts'
    # Redirect unauthenticated users to login page
    login_url = 'login'
    redirect_field_name = 'next'
    ordering = ['-published_date']
    

class RegisterView(FormView):
    template_name = 'blog/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            login(request=self.request, user=user)
        return super().form_valid(form)

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

 
class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'blog/profile.html'
    pk_url_kwarg = 'id'
    # Redirect Unauthenticated user
    login_url = reverse_lazy('login')
    context_object_name = 'user'

    def get_queryset(self):
        user_id = self.request.user.id
        user = super().get_queryset().filter(id=user_id)
        print(user)
        return user
    
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

class UserPageView(LoginRequiredMixin, generic.ListView):
    template_name = 'blog/user_posts.html'
    model = Post
    context_object_name = 'user_posts'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        author_id = self.kwargs['id']
        user_posts = super().get_queryset().filter(author=author_id)
        return user_posts

[generic.CreateView]
[generic.UpdateView]
[generic.DeleteView]
@login_required(login_url=reverse_lazy('login'))
def createpostview(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            today = datetime.today()
            post = Post.objects.create(title=title, content=content, author=author, published_date=today)
            form.save(post)
            print('Post saved!')
            return redirect('home')
    form = CreatePostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        if post:
            form = UpdatePostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home')
        form = UpdatePostForm(instance=post)
        return render(request, 'blog/edit_post.html', {'form': form, 'post': post})
    
@login_required
def delete_post(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id = pk)
        if post and post.author == request.user:
            post.delete()
    return redirect ('home')
