from django import forms


class UserForm(forms.Form):
    login = forms.CharField(max_length=30, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')


class RecipeForm(forms.Form):
    name = forms.CharField(max_length=50, label='Название')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Описание')
    cooking_steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Шаги приготовления')
    cooking_time = forms.IntegerField(label='Время приготовления в минутах')
    image = forms.ImageField(required=True, label='Изображение')


class ImageForm(forms.Form):
    image = forms.ImageField()
