from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, RecipeForm, forms
from .models import Recipes
from random import choice
from django.contrib.auth.models import User

def index(request):
    recipes = Recipes.objects.all()
    random_recipes = []
    while len(random_recipes) < 6:
        rec = choice(recipes)
        if rec not in random_recipes:
            random_recipes.append(rec)
    return render(request, 'main/index.html', {'recipes': random_recipes})


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            login = request.POST['login']
            password = request.POST['password']
            user = User.objects.create_user(username=login, password=password)
            user.save()
            return redirect('/personal_area/')
        return HttpResponse('Ошибка валидации')
    else:
        form = UserForm()
        message = 'Заполните форму регистрации'
        return render(request, 'main/login.html', {'form': form, 'message': message})


def personal_area(request):
    recipes = Recipes.objects.filter(author=request.user.pk)
    return render(request, 'main/personal_area.html', {'recipes': recipes})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST['name']
            description = request.POST['description']
            cooking_steps = request.POST['cooking_steps']
            cooking_time = request.POST['cooking_time']
            image = form.cleaned_data['image']
            author = request.user.pk
            recipe = Recipes(name=name,
                             description=description,
                             cooking_steps=cooking_steps,
                             cooking_time=cooking_time,
                             image=image,
                             author=author)
            recipe.save()
            return redirect('/personal_area/')
        return HttpResponse('Ошибка валидации')
    else:
        form = RecipeForm()
        message = 'Добавление рецепта'
        return render(request, 'main/add_recipe.html', {'form': form, 'message': message})


def all_recipes(request):
    recipes = Recipes.objects.all()
    return render(request, 'main/all_recipes.html', {'recipes': recipes})


def update_recipe(request, pk):
    recipe = Recipes.objects.filter(pk=pk).first()
    form = RecipeForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        image = form.cleaned_data['image']
        if isinstance(image, bool):
            image = None
        if image is not None:
            fs = FileSystemStorage()
            fs.save(image.name, image)
        recipe.name = form.cleaned_data['name']
        recipe.description = form.cleaned_data['description']
        recipe.cooking_steps = form.cleaned_data['cooking_steps']
        recipe.cooking_time = form.cleaned_data['cooking_time']
        recipe.image = form.cleaned_data['image']
        recipe.save()
        return redirect('/personal_area/')
    else:
        form = RecipeForm(initial={'name': recipe.name,
                                         'description': recipe.description,
                                         'cooking_steps': recipe.cooking_steps,
                                         'cooking_time': recipe.cooking_time,
                                         'image': recipe.image})

    return render(request, 'main/add_recipe.html', {'form': form})


def all_recipes(request):
    recipes = Recipes.objects.all()
    return render(request, 'main/all_recipes.html', {'recipes': recipes})


def full_recipe(request, pk):
    recipe = Recipes.objects.get(pk=pk)
    return render(request, 'main/full_recipe.html', {'recipe': recipe})