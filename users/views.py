from django.shortcuts import render, redirect ,  get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout
from .forms import ResourceForm
from django.contrib.auth.decorators import login_required
from .models import Resource

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "❌ Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ Username already exists!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "⚠️ Email is already registered!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        print("✅ User created:", user.username)

        messages.success(request, "✅ Account created successfully! You can now log in.")
        return redirect('login')

    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')


@login_required
def upload_resource(request):
    if not request.user.is_superuser:  # Only superusers allowed
        messages.error(request, "❌ You do not have permission to upload resources.")
        return redirect('home')
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploaded_by = request.user
            resource.save()
            messages.success(request, "Resource uploaded successfully!")
            return redirect('home')
    else:
        form = ResourceForm()
    return render(request, 'upload.html', {'form': form})

def contacts(request):
    return render(request,'contacts.html')
def about(request):
    return render(request,'about.html')

from .models import Resource

def resource_list(request):
    resources = Resource.objects.all().order_by('-uploaded_at')
    return render(request, 'resources.html', {'resources': resources})

from django.shortcuts import render, get_object_or_404
from .models import Resource

def view_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    return render(request, 'view_resource.html', {'resource': resource})


