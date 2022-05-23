from email import message, utils
from django.shortcuts import render, redirect
from app_second import models, utils
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from . import forms
#logic here
class Todo: 
    def __init__(self, description, name="name1"): 
        self.description = description
        self.name = name
    def counter(self, external_value): 
        self.value += external_value
    @staticmethod 
    def count(value, extra): 
        return value + extra

def index(request):
    return render(request, 'app_second/pages/index.html')

def home(request): 
    return render(request, "app_second/pages/home.html")

#user create
def user_create(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            username = form.cleaned_data['username']
            email = request.POST.get("email", "")
            password = form.cleaned_data['password1']
            user = authenticate(username=username, email=email, password=password)
            login(request,user)
            print("success")
            return redirect('home')
        else: 
            form = UserCreationForm()
    return render(request, 'app_second/pages/home.html', {'form': form})

def about(request):
    return render(request, 'app_second/pages/about.html')

def login_user(request): 
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("success")
            return redirect('home')
        else: 
            messages.add_message(request, messages.INFO, 'login failed...', extra_tags='dragonball')

            print("failure")
            return redirect('login_user')
    context = {}
    return render(request, 'app_second/pages/login.html', context)   

def logout_user(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'you logged out')
    return redirect('home')

def todo_detail(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    context = {
        "todo": obj
    }

    return render(request, 'app_second/pages/DetailTodo.html', context)


def todo_list(request):
    page_obj = utils.CustomPaginator.get_page(
        objs=models.Task.objects.all(),
        limit=2,
        current_page=request.GET.get('page')
    )
    context = {"list": None, "page": page_obj}
    return render(request, 'app_second/pages/todo_list.html', context)

def todo_create(request):
    form = forms.CreateTodo(request.POST)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('todo_list')
    else: 
        form = forms.CreateTodo()

    return render(request, 'app_second/pages/CreateTodo.html', {'form': form})

def todo_delete(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    obj.delete()
    return redirect(reverse('todo_list', args=()))
def todo_update(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    # obj.is_completed = not obj.is_completed
    if obj.is_completed:
        obj.is_completed = False
    else:
        obj.is_completed = True
    obj.save()
    return redirect(reverse('todo_list', args=()))

def todo_change_data(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    if request.method == "POST":
        title1 = request.POST.get("title", "header by default")
        description1 = request.POST.get("description", "description by default")
        obj = models.Task.objects.get(id=todo_id)

        obj.title = title1
        obj.description = description1
        obj.save()


    context = {
        "todo": obj
    }
    return render(request, 'app_second/pages/ChangeTodo.html', context)


    
