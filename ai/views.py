# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .image_recognition import predict_image
import os
from django.core.mail import send_mail
from .forms import *


@login_required
def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)

    context = {
        'profile': profile,
        'title': profile.user
    }
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request, slug):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', slug=slug)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form, 'title': profile.user})


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Сообщение от {}'.format(name),
                message,
                email,
                ['no_reply@example.com'],
                fail_silently=False,
            )
            return render(request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})


def print_letter(self, result):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    self.line.setText(letters[result])
    return letters[result]


def handle_uploaded_file(f):
    with open('temp_image.jpeg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return 'temp_image.jpeg'


def home(request):
    if request.method == 'POST':
        # Если получен POST-запрос, обрабатываем загрузку изображения и предсказание
        if 'image' in request.FILES:
            image_path = handle_uploaded_file(request.FILES['image'])
            prediction = predict_image(image_path)
            os.remove(image_path)  # Удалить временный файл после использования
            return JsonResponse({'prediction': prediction})
        else:
            return JsonResponse({'error': 'No image uploaded'}, status=400)
    else:
        # Если это GET-запрос, просто отображаем шаблон страницы
        return render(request, 'home.html')


def success(request):
    return render(request, 'success.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form, 'title': 'Регистрация'})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')  # замените 'home' на URL вашей домашней страницы
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'Авторизация'})


def logout(request):
    auth_logout(request)
    return redirect('login')

