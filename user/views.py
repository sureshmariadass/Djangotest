from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate
from user.forms import EditProfileForm,RegistrationForm
from django.contrib.auth import update_session_auth_hash
from course.models import CourseDetails
from messenger.models import Contact
from django.contrib import messages as info
# Create your views here.
def blog(request):
     return render(request,'blog-single.html')
def index(request):
    blogs=CourseDetails.objects.all()
    blogs1=blogs.filter(category__category__icontains="Trainocate")
    blogs2=blogs.filter(category__category__icontains="Cisco")
    blogs3=blogs.filter(category__category__icontains="Microsoft")
    if request.method == 'POST':

        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        c=Contact()
        c.name=name
        c.email=email
        c.subject=subject
        c.messages=message
        c.save()

        info.success(request, 'Message sent successfully.')
    context={
    'blogs1':blogs1,
    'blogs2':blogs2,
    'blogs3':blogs3
    }
    return render(request,'index.html',context)
def login(request):
     return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:

            return redirect('/profile/password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
