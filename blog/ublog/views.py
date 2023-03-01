from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from .models import BlogEntryModel
from .forms import UserRegisterForm, UserLoginForm, BlogEntryForm


class Register(View):
    form_class = UserRegisterForm
    context = {}
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class Login(View):
    form_class = UserLoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            print(user)
            if user is not None:
                login(request, user)
                print('login succesful')
                return redirect('blog')
        message = 'Login failed'
        context = {
            'form': form,
            'message': message,
        }
        return render(request, self.template_name, context)


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/')


class Main(View):
    template_name = 'main.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class Blog(View):
    template_name = 'blog.html'
    context = {}
    form_class = BlogEntryForm

    def get(self, request):
        form = self.form_class
        entrys = BlogEntryModel.objects.all()
        context = {
            'entrys': entrys,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('blog')


class Edit(UpdateView):

    template_name = 'edit.html'
    model = BlogEntryModel
    fields = ['body', ]
    success_url = "/blog"


class DeletePost(DeleteView):
    model = BlogEntryModel
    success_url = reverse_lazy('blog')
    template_name = 'confirm_delete.html'
