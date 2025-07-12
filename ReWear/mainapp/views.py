from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item,ItemImage
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import UserProfile, Item
from .forms import ProfileUpdateForm

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

        item = Item(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            size=request.POST.get('size'),
            condition=request.POST.get('condition'),
            user=request.user,
            status=True,  # Assuming you want it available by default
            points=0,    # Set default points or calculate as needed
        )
        item.save()
        # Handle multiple image uploads
        images = request.FILES.getlist('image')
        for i, img in enumerate(images[:5]):  # Limit to 5 images
            ItemImage.objects.create(user=request.user,item=item, image=img)

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

def list_item_view(request):
    item_list = Item.objects.prefetch_related('images').all()
    paginator = Paginator(item_list, 12)  # Show 12 items per page
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)
    return render(request, "list_item.html", {'items': items})

from django.shortcuts import render, get_object_or_404

def item_detail_view(request, item_id):
    item = get_object_or_404(Item.objects.prefetch_related('images'), id=item_id)
    context = {
        'item': item,
        'owner': item.user  # Assuming you want to show owner info
    }
    return render(request, "Items_detail_page.html", context)

@login_required
def user_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    
    user_items = Item.objects.filter(user=request.user).order_by('-uploaded_at')
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    
    context = {
        'profile': profile,
        'form': form,
        'user_items': user_items[:8],  # Show latest 8 items
        'total_items': user_items.count()
    }
    return render(request, 'user_profile.html', context)