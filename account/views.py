from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Register
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileForm, UserForm
from django.utils import timezone

def home(request):
    return render(request, 'index.html')

class RegisterView(View):
    def post(self,request, *args, **kwargs):
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        user_type = request.POST["user_type"]
        password = request.POST["password"]
        password1 = request.POST["password1"]
        
        if not password == password1:
            messages.warning(request, "password not matching")
            return redirect(".")

        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email, password=password)
        user.save()

        reg = Register(user=user, mobile=mobile, user_type=user_type)
        reg.save()
        messages.success(request, "User created successfully")
        return redirect("/account/login/")


    def get(self,request, *args, **kwargs):
        return render(request, 'account/account_register.html')

class LoginView(View):
    def post(self,request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"logged in successfully")
            return redirect("/")
        else:
            messages.warning(request,"invalid credentials")
            return redirect(".")

    def get(self,request, *args, **kwargs):
        return render(request, 'account/account_login.html')

class LogoutView(View):
    def get(self,request, *args, **kwargs):
        logout(request)
        messages.success(request,"logged out successfully")
        return redirect("/account/login/")

class ProfileView(View):
    def post(self,request,pk):
        user = get_object_or_404(User, pk=pk)
        u_form = UserForm(request.POST,instance=user)
        p_form = ProfileForm(request.POST, request.FILES, instance=user.register)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "updated successfully")
            return redirect(".")
        else:
            messages.info(request, "Form is not valid")
            return redirect(".")

    def get(self,request, pk,):
        # user = get_object_or_404(User, pk=pk)
        user = User.objects.filter(pk=pk)[0]
        profile = Register.objects.get(user=user)
        u_form = UserForm(instance=user)
        p_form = ProfileForm(instance=user.register)

        context = {
            'u_form':u_form,
            'p_form':p_form,
        }
        return render(self.request, 'account/profile.html', context)