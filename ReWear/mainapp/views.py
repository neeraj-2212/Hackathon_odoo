from django.contrib.auth import authenticate, login  # ✅ keep this
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):  # ✅ Rename view function to avoid conflict
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # ✅ Now this works correctly
            return redirect('landing')
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')

def landing_page(request):
    return render(request,"landing_page.html")