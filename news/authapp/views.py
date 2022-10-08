from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
# Create your views here.




# class LoginView(TemplateView):
#     template_name = "login.html"

#     def get(self, request):
#         return render(request, self.template_name, locals())



class LoginView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name, locals())

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,'======username')
        print(password,'======password')

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



