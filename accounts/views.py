from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form}) 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Thông tin đăng nhập không hợp lệ.'})
    form = AuthenticationForm()  # Tạo biểu mẫu đăng nhập
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("login")


def home_view(request):
    return render(request, 'home.html')