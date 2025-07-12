from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item,ItemImage
from django.contrib import messages

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def add_item_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        size = request.POST.get('size')
        condition = request.POST.get('condition')

        item = Item.objects.create(
            title=title,
            description=description,
            category=category,
            size=size,
            condition=condition,
            user=request.user,
            status=False
        )

        for i in range(5):  # Up to 5 images
            img = request.FILES.get(f'image{i}')
            if img:
                ItemImage.objects.create(item=item, image=img)

        messages.success(request, "Item uploaded successfully. Awaiting admin approval.")
        return redirect('landing')

    return render(request, 'add_items.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing')
            else:
                messages.error(request, 'Invalid credentials.')
        except User.DoesNotExist:
            messages.error(request, 'User not found.')
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email.split('@')[0]

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created. Please login.')
            return redirect('login')

    return render(request, 'register.html')
