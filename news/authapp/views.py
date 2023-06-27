from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from dashboard.models import *
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
# Create your views here.



class LoginView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name, locals())

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            userauth = authenticate(username=user.username, password=password)

            if userauth:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('reporter_list'))
            else:
                messages.error(request,'Invalid credentials.')

        except User.DoesNotExist:
            messages.error(request, 'username doesnot exists.')
        except Exception as e:
            raise e
            messages.error(request, str(e))

        return HttpResponseRedirect(reverse('login'))



class ForgotPass(TemplateView):
    template_name = "forgot_password.html"

    def get(self, request):
        return render(request, self.template_name, locals())


    def post(self,request):
        email = request.POST.get('email')

        try:
            filter_user = User.objects.get(email = email)
            
            code = (random.randint(1000,9999))

            ForgotPassword.objects.filter(user = filter_user).delete()

            forgot = ForgotPassword.objects.create(
                code = code,
                user = filter_user,
                )
            body = f'<a href="{request.scheme}://{request.get_host()}/change-password/{code}">Link</a>'
            # print("absolute uri: ", request.scheme)
            # print(dir(request))
            send_mail(
                "Password Reset",
                body,
                "manmeet.dev@gmail.com",
                ["meetdhanju891@gmail.com"],
                fail_silently=False,
            )
            messages.success(request, 'Mail Send Successfully.')
        except User.DoesNotExist:
            messages.info(request, 'Password update success.')


        return HttpResponseRedirect(reverse('forgot_password'))





class EditPassword(TemplateView):
    template_name = "change_password.html"
    
    def get(self, request, code):
        Grades = ForgotPassword.objects.get(code=code)
        return render(request, self.template_name, locals())

    
    def post(self, request, code):
        password = request.POST.get('password')    
        conpass = request.POST.get('confirm password')

        try:
            Grades = ForgotPassword.objects.get(code=code)
            user = Grades.user 
            user.set_password(password)
            user.save()
            Grades.delete()
        except ForgotPassword.DoesNotExist:
            messages.error(request,'some error')
                                             
        return HttpResponseRedirect(reverse('login'))
      

      
class LogoutView(TemplateView):
    
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))




class SignUpView(TemplateView):
    template_name = "register.html"

    def get(self, request):
        return render(request, self.template_name, locals())

    def post(self, request):
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            Grades = User.objects.get(email = email)
            messages.error(request,'Email already exists')

        except User.DoesNotExist:
            grades = User.objects.create(
                username = email,
                first_name = first,
                last_name = last,
                email = email
                )

            grades.set_password(password)
            grades.save()
        return HttpResponseRedirect(reverse('signup'))