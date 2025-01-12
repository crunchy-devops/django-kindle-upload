# fileupload/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UploadFileForm
from .models import UploadedFile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload')
    return render(request, 'login.html')

def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = UploadFileForm()
    
    files = UploadedFile.objects.all()
    return render(request, 'upload.html', {'form': form, 'files': files})

def logout_view(request):
    logout(request)
    return redirect('login')

