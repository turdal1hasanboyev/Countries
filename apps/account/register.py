from django.views import View

import re

from django.shortcuts import render, redirect

from django.contrib.auth import login

from django.contrib import messages

from .models import CustomUser


class RegisterView(View):
    """
    View to handle user registration.
    """

    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        
        # ✅ Emailni tekshirish
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            messages.error(request, "Invalid email format.")
            return redirect("register")
        
         # ✅ Parollarni tekshirish
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect("register")
        
        if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
            messages.error(request, "Password must contain at least one letter and one number.")
            return redirect("register")
        
        user = CustomUser.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            description=description,
            image=image,
            password=password,
        )
        user.save()
        messages.success(request, 'Registration successful')
        """
        * To'g'ridan to'g'ri login qilib yuborish va saytga kiritib yuborish
        user.save()
        messages.success(request, 'Registration successful')
        login(request, user)
        return redirect('profile')
        # Profile sahifasiga yo'naltirilmoqda
        * Foydalanuvchini saqlab login qilmasdan login sahifasiga yo'naltirib yuborish
        user.save()
        messages.success(request, 'Registration successful')
        return redirect('login')
        """
        login(request, user)
        return redirect('profile')
